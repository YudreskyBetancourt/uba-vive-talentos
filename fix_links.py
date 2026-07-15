import os
import re

files = ['dashboard.html', 'perfil.html', 'index.html', 'login.html', 'registro.html']

for file in files:
    if os.path.exists(file):
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # In the sidebar (or anywhere), find Retos Académicos and update href
        content = re.sub(r'<a href="[^"]*"( class=".*?")?>([^<]*<i class="fa-solid fa-rocket"></i> Retos Académicos)</a>', 
                         r'<a href="retos.html"\1>\2</a>', content)
        
        # Do the same for Aliados Comerciales
        content = re.sub(r'<a href="[^"]*"( class=".*?")?>([^<]*<i class="fa-solid fa-handshake"></i> Aliados Comerciales)</a>', 
                         r'<a href="aliados.html"\1>\2</a>', content)
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)

print("Enlaces de la barra lateral actualizados en todos los archivos.")
