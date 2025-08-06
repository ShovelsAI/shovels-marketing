# Shovels.ai Marketing Site

This is a static site generated with [Pelican](https://docs.getpelican.com/en/4.5.1/quickstart.html). 

### Prerequisites (assuming VS Code)

1. Install `Git` for VS Code
2. Update missing python packages for any missing dependencies (via homebrew, if Mac OS)
   a. including `npm` for Node.js

## Installation

1. Clone the `shovelsAI/shovels-marketing` githup repo
  i. validate Github user
  ii. Install Homebrew
  ii. `brew install node`
2. Fork a branch of `shovels-marketing/main`
3. Create a [Virtual Environment](https://code.visualstudio.com/docs/python/environments#_create-a-virtual-environment-in-the-terminal) in the VS Code Terminal

   a. (For Mac) `python3 -m venv .venv`

   b. Activate the virtual environment, with the following command:

     ```
     source .venv/bin/activate
     ```
   c. Confirm it's active in the terminal. It should show `(.venv) $ shovels-marketing`

**Notes**: if your named virtual environment is anything other than `venv` or `.venv`, please ask to have the [Ignore](/.gitignore) page updated accordingly. 

## Development

For initial installation, execute these three commands to download required dependencies and Pelican. 

```
pip3 install -r requirements.txt
npm i
pelican -lr
```

This will compile the static site into your `output` folder and host a simple HTTP server at that location. The console output will provide you with a link.

This installation process should **not** need to be repeated, unless you rebuild your cloned repo, virtual environment, or editor. 

Note that for development purposes, it would be the `themes/shovels` folder that you would need to interact with. `docs/` should not be modified manually. Read more under the Production section below.

For pages that have an 'inverted' theme, the logic of that inversion is done via 2 places:

- based on the route, through a script tag in `base.html` which applies a `.inverted` class to the body if it is a route that uses an inverted theme
- through tailwind utility classes using the `.inverted` parent selector in `input.css`

### New blog post

To make changes to interior pages, we use the `/content` folder. This is structured as follows:

```
/images -- contains the images for the posts
/pages -- contains the static content
/pdfs -- contains PDFs for downloading
/posts -- contains the blog posts
```

We'll just use the `/images` and `/posts` folders to make a new blog post.

Start by adding a new file to the `/posts` folder. I sometimes duplicate an existing file. 

All pages in the post folder should have the same headers. 

```markdown
Title: Shovels partners with Autodesk Construction Cloud
Subtitle: Get permit data in Autodesk Construction Cloud
Date: 2024-8-9
Modified: 2024-8-9
Category: Company
Tags: construction software, autodesk construction cloud,
Authors: Ryan Buckley
Summary: The Shovels API provides an intuitive platform for proptech enthusiasts looking to leverage building permit data. Users can access and filter building activities via types or specific date ranges. The API employs 'tags' to categorize 33 distinct types of building activities.
Image: /images/autodesk.png
```

Edit these and put the markdown content below this settings section.

Once the .md file is committed and merged into `/shovels-marketing/main`, view the output locally in your browser at `http://127.0.0.1:8000/` to verify formatting and rendering. 

### Making CSS change

To edit CSS, make changes to the `input.css` file in the root directory. It will get compiled into the final `output.css` file that the website will render locally and in production. 

> This is the only place you should edit CSS!

## Production

We currently host on GitHub Pages in the ShovelsAI GitHub organization. The site is automatically deployed using GitHub Actions whenever changes are pushed to the `main` branch.

### Automatic Deployment

The site is automatically built and deployed when you:
1. Push changes to the `main` branch
2. Open a pull request to `main` (for preview)

The GitHub Actions workflow handles:
- Installing Python and Node.js dependencies
- Building the Tailwind CSS
- Generating the static site with Pelican
- Deploying to GitHub Pages

