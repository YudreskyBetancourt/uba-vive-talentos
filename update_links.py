import os
import re

files = [f for f in os.listdir() if f.endswith('.html')]
for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Change Mi Plataforma button link to login
    content = re.sub(r'href="dashboard\.html"([^>]*class="btn-(?:login|gold)")', r'href="login.html"\1', content)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
