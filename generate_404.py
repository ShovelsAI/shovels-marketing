#!/usr/bin/env python3
"""
Script to generate 404.html page for the Shovels marketing site.
This should be run after building the site to ensure the 404 page is up to date.
"""

import os
from jinja2 import Environment, FileSystemLoader
from pelican.settings import read_settings

def generate_404():
    """Generate the 404.html page using the template."""
    try:
        # Load Pelican settings
        settings = read_settings('pelicanconf.py')
        
        # Set up Jinja2 environment
        template_dir = 'themes/shovels/templates'
        env = Environment(loader=FileSystemLoader(template_dir))
        
        # Load the 404 template
        template = env.get_template('404.html')
        
        # Render the template with Pelican settings
        html_content = template.render(
            SITENAME=settings['SITENAME'],
            SITEURL=settings['SITEURL'],
            article=None,
            page=None
        )
        
        # Write to output directory
        os.makedirs('output', exist_ok=True)
        with open('output/404.html', 'w') as f:
            f.write(html_content)
        
        # Also copy to docs directory for production
        os.makedirs('docs', exist_ok=True)
        with open('docs/404.html', 'w') as f:
            f.write(html_content)
        
        print('✅ 404.html generated successfully!')
        print(f'📁 File size: {os.path.getsize("output/404.html")} bytes')
        print('📁 Copied to both output/ and docs/ directories')
        
    except Exception as e:
        print(f'❌ Error generating 404.html: {e}')
        return False
    
    return True

if __name__ == '__main__':
    generate_404()
