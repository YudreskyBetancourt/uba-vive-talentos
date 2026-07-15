import os
import glob

html_files = glob.glob('*.html')
for html_file in html_files:
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'href="styles.css"' in content:
        content = content.replace('href="styles.css"', 'href="styles.css?v=2"')
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(content)
print('Updated styles cache')
