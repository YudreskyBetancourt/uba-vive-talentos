import re
import glob

# 1. Fix search bar flex wrap in all HTML files
files = glob.glob('*.html')
for file in files:
    try:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # If it has the search bar container, add flex-wrap: wrap
        content = content.replace('display: flex; gap: 10px; width: 100%; max-width: 600px;', 
                                  'display: flex; flex-wrap: wrap; gap: 10px; width: 100%; max-width: 600px;')
        content = content.replace('display: flex; gap: 10px; width: 100%; max-width: 700px;',
                                  'display: flex; flex-wrap: wrap; gap: 10px; width: 100%; max-width: 700px;')
        
        # Make the button full width on mobile or just pad it right
        content = content.replace('padding: 15px 35px; font-weight: 800; font-size: 15px; cursor: pointer;',
                                  'padding: 15px 35px; font-weight: 800; font-size: 15px; cursor: pointer; flex: 1; min-width: 150px;')
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
    except Exception as e:
        print(f"Error {file}: {e}")

# 2. Remove landing-navbar from all sidebar pages
for file in files:
    if file not in ['index.html', 'login.html', 'login-aliado.html', 'login-jurado.html', 'registro.html', 'registro-aliado.html', 'registro-jurado.html']:
        try:
            with open(file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if 'landing-navbar' in content:
                # Remove the nav block
                content = re.sub(r'<nav class="landing-navbar".*?</nav>', '', content, flags=re.DOTALL)
                with open(file, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Removed landing-navbar from {file}")
        except Exception as e:
            print(f"Error removing navbar {file}: {e}")

# 3. Update cache to v8
for file in files:
    try:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        content = content.replace('styles.css?v=7', 'styles.css?v=8')
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
    except Exception as e:
        pass
print("Done fixing search bar and removing landing-navbar. Cache updated to v8.")
