---
name: publish-blog
description: "Publish a blog post from Notion to the shovels-marketing Pelican site. Downloads Notion content as a .md file, creates a git branch, formats to Pelican standards, applies content guidelines, and launches a dev server preview. Trigger: /publish-blog [notion-url-or-page-name]"
version: 2.1
last_updated: 2026-03-16
patterns:
  - "publish.*(blog|post)"
  - "publish-blog"
  - "notion.*blog.*(publish|export|pelican)"
  - "blog.*(notion|draft).*(publish|post|site)"
---

# publish-blog

End-to-end pipeline: Notion draft → formatted Pelican post → git branch → dev server preview → PR.

## Prerequisites

Before starting, verify the following are installed and available. If any are missing, stop and inform the user before proceeding.

- **`uv`** — Python package manager used by the repo. Check with `uv --version`. If not installed: `curl -LsSf https://astral.sh/uv/install.sh | sh`
- **`gh`** — GitHub CLI for creating PRs. Check with `gh --version`. If not installed: `brew install gh`
- **`git`** — Must be authenticated and have push access to `shovels-marketing`
- **Notion MCP** — Only needed for page lookup/search; the `.md` export is the content source of truth

## Constants

- **Repo**: `~/Documents/GitHub/shovels-marketing`
- **Posts dir**: `content/posts/`
- **Blog images dir**: `content/images/blog_images/`
- **Content guidelines**: `CONTENT_GUIDELINES.md` (in repo root)
- **Dev server**: `make devserver` (runs at `http://localhost:8000`)

## Author Lookup Table

Use this static table as the **authoritative source** for author metadata. Do NOT infer, normalize, or look up author details from other posts in the repo. Do NOT override these values with anything found in the Notion export.

| Author Name | `author_image` | `author_title` |
|---|---|---|
| Morgan Friberg | `/theme/images/team/morgan.svg` | VP of Marketing |
| Ruoji Tang | `/theme/images/team/Ruoji.svg` | Senior Marketing Manager |
| Ryan Buckley | `/theme/images/team/ryan.svg` | CEO |
| Betty Wan | `/theme/images/team/betty.svg` | VP of Business Development & Partnerships |
| Chloe Harris | `/theme/images/team/chloe.gif` | Project Manager |

**Author rules:**
- Look up the author by name exactly as written in the Notion `.md` file
- If the author is in the table, use the table values — these are final, do not ask the user to choose between these and Notion values
- If the author is NOT in the table, ask the user for their `author_image` path and `author_title` before proceeding
- NEVER infer author info from other posts in the repo

## Pelican Frontmatter Template

```markdown
title: [Page title from Notion]
subtitle: [One-line subtitle]
date: YYYY-MM-DD
modified: YYYY-MM-DD
category: [Data | Company | Product | Industry]
tags: [Tag1, Tag2, Tag3]
authors: [Author Name]
author_image: /theme/images/team/[name].svg
author_title: [Job Title]
slug: [url-friendly-slug]
summary: [2-3 sentence meta description for search/social]
image: /images/blog_images/[hero-image.jpg]
```

**Required fields**: `title`, `date`, `slug`, `authors`, `author_image`, `author_title`

**Missing field handling**:
- If any required field is absent, ask the user before proceeding
- Present helpful suggestions where applicable (e.g., 2-3 slug options from the title)
- Example: "The `category` field is missing. Based on the content, this looks like a Data post. Should I use `category: Data`?"

## Copy Preservation Rule

**NEVER rewrite, improve, summarize, or alter ANY content without asking first.** The Notion `.md` export is the final draft. Your job is formatting only.

**This applies to:**
- Body copy (paragraphs, headings, lists, tables)
- Frontmatter values (title, subtitle, summary)
- Image captions and alt text

**What you CAN do without asking:**
- Convert syntax (images, links, callouts, embeds)
- Strip Notion artifacts (dividers, aside tags, social copy sections, trailing emojis converted per emoji rule)
- Format/structure transformations

**What you MUST ask about:**
- Changing any text content, even if you think it's wrong
- Filling in missing frontmatter fields
- Any edit that changes meaning or wording

## Image Rules

### Inline body images
Reference syntax: `{static}/images/blog_images/[filename]`

### Hero/cover image (frontmatter `image:` field)
Reference syntax: `/images/blog_images/[filename]` (no `{static}`)

### Hero image deduplication
If the Notion cover image also appears as the first image in the body content, **remove it from the body**. It should only appear in frontmatter. A hero image appearing twice (top of page + body) is a known bug — prevent it at the source.

### Image naming convention
`[blog-slug]-[short-description].[ext]`

Examples:
- `construction-leads-hero.jpg`
- `construction-leads-google-search.png`
- `construction-leads-dashboard.png`

Use the alt text or Notion caption as the description component. If neither is present, use positional fallback: `[slug]-1.jpg`, `[slug]-2.jpg`.

### Image captions
By default, preserve Notion image captions as visible text below images in italics, and as alt text in the markdown image syntax:

```markdown
![caption text]({static}/images/blog_images/filename.jpg)
*caption text*
```

This ensures accessibility (alt text) and provides context for readers (visible caption).

**If caption is missing:**
Auto-generate descriptive alt text based on:
1. Image content (if visually apparent - charts, screenshots, photos)
2. Surrounding context (paragraph before/after the image)
3. Image filename

Format: `![Auto-generated description based on context]({static}/images/blog_images/filename.jpg)`

Do NOT add the visible italic caption below if it was auto-generated - only add visible captions if they came from Notion.

### Caption suppression for graphs

Apply this convention when processing Notion captions:

- If a caption **starts with "graph"** (case-insensitive, e.g., "Graph showing permit counts by state"), **suppress the visible italic caption** — do not render `*caption text*` below the image. Still use it as the alt text in the `![]()` syntax.
- All other captions should be preserved as both alt text and a visible italicized caption.

This gives the team a simple way to control caption display without Claude needing to visually interpret image types.

### GIF and Video Handling

**GIF files:**
- Treat GIFs like any other image format
- Download, rename per naming convention, and reference using standard `{static}` syntax
- No special handling required

**MP4 files:**
- When an mp4 file is detected in the Notion export, **pause before processing** and ask the user:
  > "I found an mp4 file: `[filename]`. Would you like me to wrap it with autoplay/loop HTML to make it act like a GIF?"
- If user says **yes**, use this HTML wrapper:
  ```html
  <video autoplay loop muted playsinline style="width:100%; max-width:800px;">
    <source src="{static}/images/blog_images/[filename].mp4" type="video/mp4">
  </video>
  ```
- If user says **no**, treat it as a standard file reference (though markdown image syntax won't work for video - flag this to the user)
- Track all mp4 files found during Step 3 and prompt about each one before Step 5 formatting

### Drop shadow flagging
After placing all images, check for any that likely have white or transparent backgrounds (screenshots, UI captures, diagrams on white). Flag these in the post-processing summary:

> ⚠️ Image `[filename]` may need a drop shadow — it appears to have a white background. Add CSS class or inline style if needed.

Do not add drop shadows automatically — flag for human review.

## Notion Content Cleanup

Apply these transformations in order when processing body content:

### Strip Notion dividers
Remove standalone `---` horizontal rule lines from the body. These are Notion section dividers and do not belong in the post. (Do not remove the frontmatter `---` separators.)

Always strip any `---` dividers that appear at the very end of the body content (after the last substantive paragraph or section). These are Notion artifacts.

### Strip social copy sections
Notion drafts often include a trailing section of LinkedIn, Twitter, or other social copy separated by a divider (`---`). These are production metadata, not blog content.

When processing the body, scan for dividers followed by social copy indicators (e.g., lines or sections containing "LinkedIn", "Twitter", "social", "caption for", "post copy", "IG", "thread"). If found:

- Remove everything from that divider onward
- Note the strip in the post-processing summary: "Stripped social copy section after final divider."

If you're unsure whether a section is social copy vs. actual content, flag it to the user rather than silently removing it.

### Emoji handling
**Keep all emojis exactly as they appear in Notion.** The Notion page is the final draft - preserve all emojis as plain Unicode characters in the markdown without any edits, removals, or conversions.

Do NOT interpret an emoji as a signal to create a callout block, `<aside>`, or any other structured formatting.

### Callout blocks and aside tags
Notion callouts may appear as either callout-block syntax or `<aside>` HTML tags in the export. Convert both to blockquotes:

```markdown
> **Note:** [callout text here]
```

Flag each converted callout in a summary at the end so the user can review.

### Arcade embed conversion
Detect any URLs containing `arcade.software` (e.g., `https://app.arcade.software/...`). Convert them from links to embedded iframes:

```html
<iframe src="[arcade-url]" frameborder="0" loading="lazy" webkitallowfullscreen mozallowfullscreen allowfullscreen style="width:100%; height:500px; border:0;"></iframe>
```

Do not leave Arcade URLs as plain links or markdown links — they must be iframes.

## Links

**All links must open in new tabs** using HTML syntax with `target="_blank"`:

```html
<a href="https://example.com/..." target="_blank">link text</a>
```

**Important rules:**
- Do NOT use markdown link syntax `[text](url)` — it doesn't support target attributes
- Keep all URLs exactly as they appear in Notion (including internal `https://www.shovels.ai/...` links)
- Convert all markdown links to HTML with `target="_blank"`

**Handling broken Notion internal links:**
If you encounter Notion internal links (e.g., `/31b5e14e73528012b972fee8528e0a2d?pvs=25`), these are broken page references. Flag them to the user and ask for the correct external URL.

**Note:** This workflow uses absolute URLs instead of Pelican's `{filename}` syntax (which CONTENT_GUIDELINES.md recommends). Absolute URLs are preferred here because they're Notion-friendly, simpler to work with, and clickable in editors.

---

## Workflow

**Progress Tracking:** At the start of each step, display a status update to show progress:

```
📍 Step [X]/9: [Step Name]
```

This helps track where we are in the publishing process and how much remains.

---

### Step 1: Get the Notion content as a Markdown file

**📍 Step 1/9: Get Notion content**

**Do NOT use the Notion API to extract body content. Do NOT run any Python processing pipeline.** Downloading directly as a `.md` file is the source of truth and avoids the formatting corruption that API extraction causes.

Ask the user to export the Notion page as Markdown:

1. Open the Notion page
2. Click the **⋯ (three-dot menu)** in the top-right → **Export**
3. Choose **Markdown & CSV** format, **current page only**
4. Unzip the downloaded file if needed
5. Drop the resulting `.md` file into the conversation (or paste its path)

Once the `.md` file is provided, use it as the raw source for all content and metadata. Do NOT re-fetch the page body from the API.

> If you need to look up the Notion page for metadata (e.g., created date, tags, or page properties not present in the export), you may use `notion-fetch` or `notion-search` for that purpose only — not for body content.

### Step 2: Extract metadata and content

**📍 Step 2/9: Extract metadata**

**First, parse Notion frontmatter:**

Check if the Notion `.md` export includes a frontmatter code block (typically appears near the top with fields like `Author:`, `Date:`, `Category:`, `Tags:`, etc.). If found, extract all available values.

**Then collect and auto-generate missing fields:**

| Field | Source | Auto-generation if missing |
|---|---|---|
| `title` | Notion page title (from `.md` file or frontmatter) | N/A - always required |
| `authors` | Notion frontmatter → Author Lookup Table → Ask user | Never infer from repo |
| `date` | Notion frontmatter or `created_time` property | Use today's date (YYYY-MM-DD) |
| `modified` | Same as `date` initially | Same as `date` |
| `slug` | Notion frontmatter → Auto-generate from title | Slugify title (lowercase, hyphens, remove special chars, suggest 2-3 options) |
| `summary` | Notion frontmatter or subtitle/description | Auto-generate 2-3 sentence meta description from first paragraph (150-160 chars for SEO) |
| `subtitle` | Notion frontmatter or subtitle property | Optional - leave blank if missing |
| `category` | Notion frontmatter → Infer from content → Ask user | Analyze content and suggest category (Data/Company/Product/Industry) |
| `tags` | Notion frontmatter or tags property | Extract 3-5 keywords from content (lowercase, hyphenated, comma-separated) |
| `image` | First image in the `.md` file body (see below) | Required - must exist |
| Body content | Full page body from the `.md` file | N/A |

**Auto-generation guidelines:**
- Always present auto-generated values to the user for approval before finalizing
- For `slug`: Offer 2-3 options derived from the title
- For `summary`: Keep under 160 characters for SEO optimization
- For `category`: Analyze post topic (data analysis → Data, company news → Company, feature launch → Product, market trends → Industry)
- For `tags`: Extract main topics as lowercase, hyphen-separated keywords (e.g., "building-permits", "solar-panels", "market-analysis")

**CRITICAL — Hero image workflow:**
The Notion export does NOT include page cover images. Instead, the team follows this standard:
- **Hero image MUST be the first image in the Notion page** (placed above the frontmatter code block)
- When you open the `.md` file, check if the first image exists in the content
- If NO first image found:
  - Ask: "I don't see a hero image. Please add it as the first image in the Notion page (above the frontmatter), re-export, and share the new `.md` file."
  - Wait for the updated file
- If first image found:
  - Download it as `[slug]-hero.[ext]`
  - Use it in frontmatter `image:` field
  - **Remove it from the body content** (hero image deduplication per Image Rules above)

**Image URLs in Notion exports are temporary (expire ~1 hour).** Proceed to Step 3 immediately after receiving the file.

### Step 3: Download and rename images

**📍 Step 3/9: Download images**

For each image/video URL found in the `.md` file:

1. Use `curl` to download immediately:
   ```bash
   curl -L "[notion-s3-url]" -o ~/Documents/GitHub/shovels-marketing/content/images/blog_images/[slug]-[description].ext
   ```

2. Determine extension from the URL or response `Content-Type` header.

3. Record the mapping: `original-notion-url → new-filename`

4. **Track mp4 files separately** — note each mp4 filename for Step 5 prompting (see "GIF and Video Handling" in Image Rules)

**Progress tracking for multiple images:**
- If 5+ images, show progress: "Downloading image 3/8..."
- If 10+ images, show progress after every 2-3 downloads

**If a download fails:**
- Report which image failed and why
- Ask the user to drop the image manually into `content/images/blog_images/` with the expected filename
- Wait for confirmation before continuing

### Step 4: Create git branch

**📍 Step 4/9: Create git branch**

**Do this before writing any files.**

```bash
cd ~/Documents/GitHub/shovels-marketing
git checkout main
git pull origin main
git checkout -b blog/[slug]
```

If a branch named `blog/[slug]` already exists, ask the user: checkout existing branch or create `blog/[slug]-v2`?

### Step 5: Format the post

**📍 Step 5/9: Format post**

**BEFORE constructing the file:**

If any mp4 files were detected in Step 3, prompt the user for each one:

> "I found an mp4 file: `[filename]`. Would you like me to wrap it with autoplay/loop HTML to make it act like a GIF?"

Record the user's decision for each mp4 file before proceeding to formatting.

**Then construct the `.md` file:**

1. Write frontmatter using the template above with all collected values
2. Add a horizontal rule separator (`---`)
3. Paste body content from the Notion export, applying these transformations in order:
   - Strip social copy sections (scan for trailing dividers followed by LinkedIn/Twitter/social content — remove from divider onward)
   - Strip Notion `---` dividers from body (preserve frontmatter separator)
   - Strip any trailing `---` dividers at the end of the body
   - Remove the hero/cover image if it appears as the first body image (deduplication)
   - Replace Notion image URLs with `{static}/images/blog_images/[new-filename]`
   - Replace hero image URL in frontmatter with `/images/blog_images/[hero-filename]`
   - **Handle mp4 files:** For each mp4 where user approved video-as-gif wrapper, replace the reference with the HTML video wrapper (see "GIF and Video Handling" in Image Rules). For mp4s where user declined, leave as standard file reference and flag for review.
   - Add image captions per caption rules above (suppress visible caption if caption starts with "graph"; otherwise add as italicized text below the image; auto-generate alt text if caption missing)
   - Keep all emojis exactly as they appear in Notion — do NOT edit, remove, or convert them
   - Convert callout blocks and `<aside>` tags to `> **Note:** [text]` blockquotes
   - Convert Arcade URLs to embedded iframes
   - Convert all markdown links `[text](url)` to HTML with `target="_blank"`: `<a href="url" target="_blank">text</a>`
   - Preserve all other formatting (headings, bold, lists, tables, code blocks)
   - **Do not alter body copy**

4. Save to: `~/Documents/GitHub/shovels-marketing/content/posts/[slug].md`

> **⚠️ The dev server does NOT hot-reload.** After saving the file, you must manually rebuild to see changes:
> ```bash
> ./venv/bin/pelican content
> ```
> Then refresh your browser. Remind the user of this any time they need to preview edits.

### Step 6: Apply content guidelines

**📍 Step 6/9: Apply content guidelines & FAQ**

**Read the content guidelines:**
```bash
cat ~/Documents/GitHub/shovels-marketing/CONTENT_GUIDELINES.md
```

**Determine FAQ eligibility:**

Review the post against the "When to Add FAQs" section in CONTENT_GUIDELINES.md:

1. Analyze the post content, category, and format
2. Check if it matches the **✅ Always Include FAQs** criteria (educational content, data analysis, product features, landing pages)
3. Check if it matches the **❌ Skip FAQs For** criteria (newsletters, announcements, podcasts, case studies, brief posts)

**If the post qualifies for an FAQ:**

Ask the user:

> "This post qualifies for an FAQ section based on the content guidelines (reason: [educational/data analysis/etc.]). Would you like me to generate an FAQ with 3-5 questions?"

If user says **yes**:
1. Check if the Notion draft already has an FAQ section
2. If FAQ exists in draft, use those Q&A pairs
3. If no FAQ exists, generate 3-5 relevant questions following the guidelines in CONTENT_GUIDELINES.md:
   - Questions start with what/how/why/when/can/does
   - Answers are 2-4 sentences (50-100 words)
   - Include specific numbers and concrete details
   - Use official stats from CONTENT_GUIDELINES.md (185M+ permits, 3.3M+ contractors, 2,000+ jurisdictions, etc.)
   - For product/API questions, base answers on information in the blog post content
   - Note: docs.shovels.ai is the source of truth for Shovels product details - if uncertain about a detail, ask the user or flag it for review
4. Present the generated FAQ to the user for approval before adding
5. Once approved, add both formats per CONTENT_GUIDELINES.md:
   - HTML FAQ section (visible on page)
   - JSON-LD schema immediately after HTML (for AI answer engines)

If user says **no**:
- Skip FAQ section
- Note in summary: "User opted to skip FAQ"

**If the post does NOT qualify for an FAQ:**
- Note in summary: "No FAQ added per content guidelines (reason: [time-sensitive/brief/story-driven/etc.])"
- Do not add FAQ section or JSON-LD schema

### Step 7: Verify and stage

**📍 Step 7/9: Stage files**

```bash
cd ~/Documents/GitHub/shovels-marketing
git add content/posts/[slug].md content/images/blog_images/
git status
```

Show the user a brief summary:
- Files added
- Image count and names (including GIF and mp4 files)
- MP4 files wrapped as video-as-gif (count and filenames)
- Image captions preserved (count), graph captions suppressed (count)
- Links converted to HTML with target="_blank" (count)
- Callouts converted (with text previews)
- Arcade embeds converted (count)
- Whether FAQ was pre-existing or auto-generated (and the Q&A pairs if generated)
- Whether social copy section was stripped
- Any images flagged for drop shadow review

Do **not** commit yet — wait for post-preview approval.

### Step 8: Launch dev server and verify build

**📍 Step 8/9: Build and preview**

**Check if dev server is already running:**
```bash
curl -s -o /dev/null -w "%{http_code}" http://localhost:8000
```

**If returns 200 (server already running):**
1. Manually rebuild the site to ensure new post is processed:
   ```bash
   cd ~/Documents/GitHub/shovels-marketing
   ./venv/bin/pelican content
   ```
2. Verify the post was built:
   ```bash
   ls -la output/blog/ | grep [slug]
   ```
3. If the directory exists, the post is ready

**If server is NOT running (connection refused):**
```bash
cd ~/Documents/GitHub/shovels-marketing
make devserver
```

**Present the preview URL and ask for next steps:**

```
Preview ready: http://localhost:8000/blog/[slug]/
```

Tell the user to open the URL in their browser and review the post. Remind them: **hard refresh with Shift+Cmd+R** if they've made manual edits and the preview looks stale. Remind them that **the dev server does not hot-reload** — any file changes require re-running `./venv/bin/pelican content` before refreshing.

**Then immediately ask:**

> Please review the post in your browser. What would you like to do next?
>
> 1. **Ready to publish?** - Reply **'approve'** and I'll commit, push, and create the PR
> 2. **Need edits?** - Describe the changes you'd like and I'll apply them
> 3. **Something broken?** - Let me know what's not working

Do not wait silently after providing the preview link — actively prompt the user for their decision.

> **Note — do NOT ask:** "Should I use the content strategist skill?" This question has confused team members and should not be asked. If you want to flag a potential content quality concern, ask specifically: e.g., "Would you like me to check this post against the brand voice guidelines before we publish?"

### Step 9: Handle feedback or approve

**📍 Step 9/9: Commit, push, and create PR**

**If changes needed:**
Apply the requested edits to the `.md` file. After each edit, remind the user to save the file and rebuild:
```bash
./venv/bin/pelican content
```
Then hard-refresh in the browser (Shift+Cmd+R). Repeat until approved.

**If approved:**
```bash
cd ~/Documents/GitHub/shovels-marketing
git add content/posts/[slug].md content/images/blog_images/
git commit -m "Add [slug] blog post"
git push origin blog/[slug]
```

Then ask: "Who should review this PR?" Wait for the user to provide a name or email before creating it.

```bash
gh pr create --title "Add [slug] blog post" --body "[brief description of post — title, image count, notable elements like Arcade embeds or FAQ]" --reviewer [reviewer-email]
```

Remind the user: after the reviewer approves, **Squash and Merge** the PR on GitHub, then delete the branch.

---

## Common Issues

**No hero image found in Notion export**
- The Notion export does NOT include page cover images
- Ask user to add hero image as first image in page content (above frontmatter), re-export, and share the new `.md` file

**New post not showing on dev server**
- The dev server does NOT auto-reload on file changes
- Manually rebuild: `./venv/bin/pelican content`
- Verify build: `ls -la output/blog/ | grep [slug]`
- If directory exists, post is ready at `http://localhost:8000/blog/[slug]/`

**Images not rendering on dev server**
- Verify the filename in the `.md` exactly matches the file in `content/images/blog_images/` (case-sensitive)
- Check `{static}` is present for body images and absent for the frontmatter `image:` field

**Dev server showing stale content after manual edits**
- Save the file (Cmd+S), then rebuild (`./venv/bin/pelican content`), then hard refresh (Shift+Cmd+R)

**Slug conflicts (post already exists)**
- Check `content/posts/` for an existing file with the same slug
- If found, confirm with user before overwriting

**Dev server port already in use**
- Server is likely already running from a previous session
- Check if it's accessible: `curl -s http://localhost:8000`
- If accessible, manually rebuild instead of starting a new server
- If not accessible, kill the process and restart

**Notion page not found**
- Confirm the user has the Notion MCP connected (needed for metadata lookup only)
- Try fetching by page ID extracted from the URL (last segment before `?`)

**Author not in lookup table**
- Ask the user for the author's `author_image` path and `author_title`
- Do not look at other posts or attempt to normalize/infer the values
- Consider adding the new author to the lookup table in this skill file for future use

**`uv` not found**
- Install with: `curl -LsSf https://astral.sh/uv/install.sh | sh`
- Then restart the terminal or run `source $HOME/.cargo/env`
