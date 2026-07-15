import os
import glob

html_files = glob.glob('*.html')
for html_file in html_files:
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'href="styles.css?v=2"' in content:
        content = content.replace('href="styles.css?v=2"', 'href="styles.css?v=3"')
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(content)
print('Updated styles cache to v3')
