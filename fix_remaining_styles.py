import re
import glob

files = ['retos.html', 'aliados.html', 'logros.html', 'vacantes.html']
extracted_styles = []

for file in files:
    try:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        matches = re.finditer(r'<style>(.*?)</style>', content, re.DOTALL)
        for match in matches:
            style_content = match.group(1)
            # Add to extracted styles
            extracted_styles.append(f"/* Extracted from {file} */\n{style_content}")
                
        # Remove the style blocks from the HTML completely
        content = re.sub(r'<style>.*?</style>', '', content, flags=re.DOTALL)
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Removed <style> blocks from {file}")
    except Exception as e:
        print(f"Error processing {file}: {e}")

if extracted_styles:
    with open('styles.css', 'r', encoding='utf-8') as f:
        css = f.read()
        
    combined_styles = "\n".join(extracted_styles)
    
    # We want to insert it right before @media (max-width: 992px)
    css = re.sub(r'(@media\s*\(max-width:\s*992px\)\s*{)', combined_styles + r'\n\1', css)
    
    with open('styles.css', 'w', encoding='utf-8') as f:
        f.write(css)
    print("Injected extracted styles into styles.css")

# One more thing: .page-layout is grid-template-columns: 2fr 1fr. 
# Did we add .page-layout to the media query in styles.css?
# Let's check styles.css to ensure .page-layout becomes 1fr on mobile.

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

if '.page-layout' not in css.split('@media (max-width: 992px)')[1]:
    responsive_css = '''
    .page-layout { grid-template-columns: 1fr !important; }
    .hero-filters { justify-content: flex-start !important; overflow-x: auto; padding-bottom: 5px; flex-wrap: nowrap !important; }
    .hero-filters span { white-space: nowrap; }
    .challenge-meta { flex-wrap: wrap; }
    '''
    css = re.sub(r'(@media\s*\(max-width:\s*992px\)\s*{)', r'\1\n' + responsive_css, css)
    with open('styles.css', 'w', encoding='utf-8') as f:
        f.write(css)
    print("Added .page-layout to mobile query")

for file in glob.glob('*.html'):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    content = content.replace('styles.css?v=8', 'styles.css?v=9')
    content = content.replace('styles.css?v=7', 'styles.css?v=9')
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
print("Updated cache to v9")
