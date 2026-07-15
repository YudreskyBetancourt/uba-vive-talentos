import os
import re

# We need to find all .html files in the directory
directory = '.'
html_files = [f for f in os.listdir(directory) if f.endswith('.html') and f != 'logros.html']

# The link we want to add:
# <a href="logros.html"><i class="fa-solid fa-award"></i> Logros Académicos</a>
# We'll insert it right after the 'Mi Perfil' link.

link_to_insert = '\n            <a href="logros.html"><i class="fa-solid fa-award"></i> Logros Académicos</a>'

for file in html_files:
    filepath = os.path.join(directory, file)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # The Mi Perfil link can have class="activo" or not.
    # Pattern to match: <a href="perfil.html".*?>.*?Mi Perfil</a>
    pattern = r'(<a href="perfil.html"[^>]*>.*?Mi Perfil</a>)'
    
    # Check if we already inserted it to avoid duplicates
    if 'href="logros.html"' not in content:
        updated_content = re.sub(pattern, r'\1' + link_to_insert, content, flags=re.DOTALL)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        print(f"Actualizado: {file}")
    else:
        print(f"Saltado (ya tiene el enlace): {file}")

print("Proceso de actualización de barra lateral completado.")
