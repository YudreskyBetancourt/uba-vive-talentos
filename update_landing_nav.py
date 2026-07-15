import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

# The replacement block
new_nav = """<div class="nav-links">
            <a href="index.html">Inicio</a>
            <a href="carreras.html">Carreras</a>
            <a href="login-aliado.html">Aliados</a>
            <a href="login-jurado.html">Jurados</a>
            <a href="login.html" class="btn-login">Mi Plataforma</a>
        </div>"""

# For pages inside the platform that have the landing navbar but shouldn't have the login button:
new_nav_inside = """<div class="nav-links">
            <a href="index.html">Inicio</a>
            <a href="carreras.html">Carreras</a>
            <a href="login-aliado.html">Aliados</a>
            <a href="login-jurado.html">Jurados</a>
        </div>"""

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the nav-links block
    pattern = r'<div class="nav-links">.*?</div>'
    
    if '<a href="login.html" class="btn-login">Mi Plataforma</a>' in content or '<a href="login.html" class="btn-login">Entrar</a>' in content:
        updated_content = re.sub(pattern, new_nav, content, flags=re.DOTALL)
    elif 'btn-login' in content:
        # If it has btn-login but different text, replace with new_nav
        updated_content = re.sub(pattern, new_nav, content, flags=re.DOTALL)
    else:
        # It's an internal page, don't show the "Mi Plataforma" button on top since there's a sidebar
        updated_content = re.sub(pattern, new_nav_inside, content, flags=re.DOTALL)
        
    if updated_content != content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        print(f"Actualizado navbar en: {file}")

print("Actualización de barra superior completada.")
