#!/usr/bin/env bash
# Cloudflare Pages preview build.
#
# Mirrors the GitHub Pages CI build (.github/workflows/deploy.yml) but:
#   - outputs to ./output (Cloudflare Pages serves this dir), and
#   - drops the GitHub-Pages-only steps (CNAME, .nojekyll).
#
# Production hosting stays on GitHub Pages and is unaffected by this script.
# Cloudflare Pages dashboard settings:
#   Build command:      bash cf-pages-build.sh
#   Build output dir:   output
#   Env vars:           PYTHON_VERSION=3.11, NODE_VERSION=18
set -euo pipefail

pip install -r requirements.txt
npm install
npm run build:css:prod
pelican content -o output -s publishconf.py
# base.html loads /theme/css/output.css (copied by the theme static path);
# this second copy mirrors CI's docs/output.css for any legacy reference.
cp themes/shovels/static/css/output.css output/output.css
