# Shovels.ai Marketing Site

This is a static site generated with Pelican. 

## Development

Do the regular initial setup. Create and activate a virtual env and then do:

```
pip3 install -r requirements.txt
npm i
pelican -lr
```

This will compile the static site into your `output` folder and host a simple HTTP server at that location. The console output will provide you with a link.

Note that for development purposes, it would be the `themes/shovels` folder that you would need to interact with. `docs/` should not be modified manually. Read more under the Production section below.

For pages that have an 'inverted' theme, the logic of that inversion is done via 2 places:

- based on the route, through a <script> in `base.html` which applies a `.inverted` class to the body if it is a route that uses an inverted theme
- through tailwind utility classes using the `.inverted` parent selector in `input.css`

### New blog post

To make changes to interior pages, we use the /content folder. This is structured as follows:

```
/images -- contains the images for the posts
/pages -- contains the static content
/pdfs -- contains PDFs for downloading
/posts -- contains the blog posts
```

We'll just use the /images and /posts folders to make a new blog post.

Start by adding a new file to the /posts folder. I sometimes duplicate an existing file. 

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

Edit these and put the markdown below this settings section.

## Production

We currently host on GitHub Pages in the ShovelsAI GitHub organization. GitHub requires the output folder to be `docs` so we have to use a different command.

To publish, simply run:
```
make publish
```
The Makefile will deal with the oddities of GitHub pages and make sure certain configs aren't lost in the process.

You can see the latest version now at https://www.shovels.ai!