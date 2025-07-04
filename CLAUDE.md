# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Development Commands

### Python Environment Setup
```bash
# Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip3 install -r requirements.txt
npm i
```

### Development Server
```bash
# Start development server with live reload
pelican -lr

# Alternative using Makefile
make devserver
```

### Building and Publishing
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

This is a **Pelican-based static site generator** for the Shovels.ai marketing website with the following key components:

### Content Structure
- **`/content/`** - All source content
  - `posts/` - Blog posts in Markdown format
  - `pages/` - Static pages (about, pricing, etc.)
  - `images/` - Image assets for posts
  - `pdfs/` - Downloadable PDF resources

### Theme System
- **`/themes/shovels/`** - Custom Pelican theme
  - `templates/` - Jinja2 HTML templates
  - `static/` - CSS, JS, images, fonts
  - Uses **Tailwind CSS** for styling with custom Shovels brand colors
  - Supports "inverted" theme pages via CSS classes and route-based logic

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

### Publishing Workflow
The `make publish` command:
1. Builds site with production config to `./docs/`
2. Copies CSS assets
3. Creates CNAME file for custom domain
4. Auto-commits and pushes to GitHub Pages

### Blog Post Creation
All blog posts require these frontmatter fields:
```yaml
Title: Post Title
Subtitle: Post Subtitle  
Date: YYYY-MM-DD
Category: Company|Data|GTM|etc
Tags: comma, separated, tags
Authors: Author Name
Summary: Brief description
Image: /images/filename.png
```

### Custom Brand Colors (Tailwind)
- Primary: `#01654D` (shovels-primary)
- Secondary: `#E9BE51` (shovels-secondary)  
- Dark: `#101727` (shovels-dark)
- Light: `#EAE2CF` (shovels-light)