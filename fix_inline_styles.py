import re
import glob

# 1. Fix inline flex in search bars
files_with_search = ['aliados.html', 'retos.html']
for file in files_with_search:
    try:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Fix the flex container
        content = content.replace('style="display: flex; background: rgba(255,255,255,0.1); padding: 10px; border-radius: 40px; margin-top: 30px;"',
                                  'class="search-hero-bar" style="display: flex; flex-wrap: wrap; gap: 10px; background: rgba(255,255,255,0.1); padding: 10px; border-radius: 20px; margin-top: 30px;"')
        # Fix the input to grow and have a minimum width so it wraps
        content = content.replace('style="flex-grow: 1; padding: 15px 25px; border-radius: 30px; border: none; font-size: 15px; outline: none; box-shadow: 0 5px 15px rgba(0,0,0,0.1);"',
                                  'style="flex-grow: 1; min-width: 200px; padding: 15px 25px; border-radius: 30px; border: none; font-size: 15px; outline: none; box-shadow: 0 5px 15px rgba(0,0,0,0.1);"')
        # Fix the button
        content = content.replace('padding: 0 35px;', 'padding: 15px 35px;')
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed search bar in {file}")
    except Exception as e:
        print(f"Error fixing {file}: {e}")

# 2. Extract <style> blocks from dashboard files and append to styles.css
dashboards = ['dashboard.html', 'dashboard-jurado.html', 'dashboard-aliado.html', 'perfil.html']
extracted_styles = []

for file in dashboards:
    try:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find all <style> blocks (there might be more than one, but usually one in head)
        matches = re.finditer(r'<style>(.*?)</style>', content, re.DOTALL)
        for match in matches:
            style_content = match.group(1)
            # Only extract if it contains profile-hero or similar specific rules, not generic resets
            if '.profile-hero' in style_content or '.card-sec' in style_content or '.corp-header' in style_content:
                extracted_styles.append(f"/* Extracted from {file} */\n{style_content}")
                
        # Remove the style blocks from the HTML completely
        content = re.sub(r'<style>.*?</style>', '', content, flags=re.DOTALL)
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Removed <style> blocks from {file}")
    except Exception as e:
        print(f"Error processing {file}: {e}")

# 3. Inject extracted styles into styles.css BEFORE the media query
if extracted_styles:
    with open('styles.css', 'r', encoding='utf-8') as f:
        css = f.read()
        
    combined_styles = "\n".join(extracted_styles)
    
    # We want to insert it right before @media (max-width: 992px)
    css = re.sub(r'(@media\s*\(max-width:\s*992px\)\s*{)', combined_styles + r'\n\1', css)
    
    with open('styles.css', 'w', encoding='utf-8') as f:
        f.write(css)
    print("Injected extracted styles into styles.css")

# 4. Update cache to v7
for file in glob.glob('*.html'):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    content = content.replace('styles.css?v=6', 'styles.css?v=7')
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
print("Updated cache to v7")
