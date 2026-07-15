import re

files_to_clean = ['dashboard.html', 'dashboard-aliado.html', 'dashboard-jurado.html', 'perfil.html']

for file in files_to_clean:
    try:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Remove landing-navbar
        content = re.sub(r'<nav class="landing-navbar">.*?</nav>', '', content, flags=re.DOTALL)
        
        # Update cache to v4
        content = content.replace('styles.css?v=3', 'styles.css?v=4')
        content = content.replace('styles.css?v=2', 'styles.css?v=4')
        content = content.replace('styles.css"', 'styles.css?v=4"')
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Cleaned {file}")
    except Exception as e:
        print(f"Error processing {file}: {e}")

# Fix styles.css
with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

bad_css_1 = '''.main-content {
        margin-left: 0 !important;
        padding-top: 80px !important; /* Espacio para el fixed top-bar */
        width: 100%;
    }'''

good_css_1 = '''.main-content, body.has-sidebar .main-content {
        margin-left: 0 !important;
        padding-top: 80px !important; /* Espacio para el fixed top-bar */
        width: 100% !important;
    }
    
    body.has-sidebar .top-bar {
        margin-left: 0 !important;
        width: 100% !important;
    }'''

if bad_css_1 in css:
    css = css.replace(bad_css_1, good_css_1)
    with open('styles.css', 'w', encoding='utf-8') as f:
        f.write(css)
    print("Fixed styles.css")
else:
    print("styles.css block not found")

# Update cache in index.html, carreras.html, etc.
import glob
for file in glob.glob('*.html'):
    if file not in files_to_clean:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        content = content.replace('styles.css?v=3', 'styles.css?v=4')
        content = content.replace('styles.css?v=2', 'styles.css?v=4')
        content = content.replace('styles.css"', 'styles.css?v=4"')
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated cache in {file}")

print("All done.")
