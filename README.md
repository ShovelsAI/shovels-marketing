# Shovels.ai Marketing Site

This is a static site generated with [Pelican](https://docs.getpelican.com/en/4.5.1/quickstart.html).

## Prerequisites

1. Install Git
2. Install Python 3
3. Install Node.js (`brew install node` on macOS)

## Installation

```bash
# Clone the repo
git clone https://github.com/ShovelsAI/shovels-marketing.git
cd shovels-marketing

# Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip3 install -r requirements.txt
npm i
```

**Note**: If your virtual environment is named something other than `venv` or `.venv`, update `.gitignore` accordingly.

## Development

### Start Development Server

```bash
make devserver
```

This runs both the Pelican live-reload server and the Tailwind CSS watcher together, compiling the site into `./output/` and hosting it at http://127.0.0.1:8000.

> **Note**: Running `pelican -lr` alone will not rebuild Tailwind CSS. Always use `make devserver` to ensure CSS changes are picked up.

### Building

```bash
# Build for development (outputs to ./output/)
pelican content -s pelicanconf.py

# Build for production (outputs to ./docs/ for GitHub Pages)
make publish

# Build CSS separately if needed
npm run build:css              # Development with watch
npm run build:css:prod         # Production minified
```

## Architecture Overview

### Content Structure

- **`/content/`** - All source content
  - `posts/` - Blog posts in Markdown format
  - `pages/` - Static pages (about, careers, etc.)
  - `images/` - Image assets for posts
  - `pdfs/` - Downloadable PDF resources

### Theme System

- **`/themes/shovels/`** - Custom Pelican theme
  - `templates/` - Jinja2 HTML templates
  - `static/` - CSS, JS, images, fonts
  - Uses **Tailwind CSS** for styling with custom Shovels brand colors
  - Supports "inverted" theme pages via CSS classes and route-based logic

For inverted theme pages, the logic is handled in two places:
- Route-based: A script tag in `base.html` applies `.inverted` class to body
- Styling: Tailwind utility classes using `.inverted` parent selector in `input.css`

### Configuration Files

- **`pelicanconf.py`** - Development configuration
- **`publishconf.py`** - Production configuration (GitHub Pages)
- **`tailwind.config.js`** - Tailwind CSS configuration with Shovels brand colors
- **`Makefile`** - Build automation commands

### Key Features

- **Dual output paths**: `./output/` for dev, `./docs/` for GitHub Pages
- **SEO optimized** with pelican-seo plugin
- **Custom URL structure**: Blog posts at `/blog/{slug}/`
- **Asset processing**: Tailwind CSS compilation and minification
- **Live reload** during development

## Blog Post Creation

Add a new file to `/content/posts/`. All blog posts require these frontmatter fields:

```yaml
Title: Post Title
Subtitle: Post Subtitle
Date: YYYY-MM-DD
Modified: YYYY-MM-DD
Category: Company|Data|GTM|etc
Tags: comma, separated, tags
Authors: Author Name
Summary: Brief description
Image: /images/filename.png
```

Put the markdown content below the frontmatter.

## Making CSS Changes

Edit the `input.css` file in the root directory, then copy it to `/themes/shovels/static/css/input.css`. It will compile into the final `output.css` file.

> This is the only place you should edit CSS!

## Production

We host on GitHub Pages in the ShovelsAI GitHub organization. The site is automatically deployed using GitHub Actions whenever changes are pushed to the `main` branch.

### Automatic Deployment

The site is automatically built and deployed when you:
1. Push changes to the `main` branch
2. Open a pull request to `main` (for preview)

The GitHub Actions workflow handles:
- Installing Python and Node.js dependencies
- Building the Tailwind CSS
- Generating the static site with Pelican
- Deploying to GitHub Pages

### Manual Publishing

The `make publish` command:
1. Builds site with production config to `./docs/`
2. Copies CSS assets
3. Creates CNAME file for custom domain
4. Auto-commits and pushes to GitHub Pages

## Brand Colors (Tailwind)

- Primary: `#01654D` (shovels-primary)
- Secondary: `#E9BE51` (shovels-secondary)
- Dark: `#101727` (shovels-dark)
- Light: `#EAE2CF` (shovels-light)
