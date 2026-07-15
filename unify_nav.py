import os
import re

css_to_add = """
/* ==========================================================================
   TOP BAR Y NAVBAR GLOBAL
   ========================================================================== */
.top-bar {
    background-color: #001a38;
    color: var(--text-light);
    font-size: 11px;
    padding: 8px 5%;
    display: flex;
    justify-content: flex-end;
    gap: 20px;
    font-weight: 600;
}
.top-bar span { cursor: pointer; transition: color 0.2s; }
.top-bar span:hover { color: var(--accent-gold); }

.landing-navbar { 
    display: flex; 
    justify-content: space-between; 
    align-items: center; 
    padding: 15px 5%; 
    background: var(--text-light); 
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    position: sticky;
    top: 0;
    z-index: 1000;
}

.logo {
    display: flex;
    align-items: center;
    gap: 15px;
}

.logo-shield {
    background: var(--primary-blue);
    color: white;
    padding: 15px 18px;
    border-radius: 0 0 15px 15px;
    font-weight: 800;
    font-size: 24px;
    text-align: center;
    margin-top: -30px;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    border: 2px solid white;
    border-top: none;
}

.logo-text h2 { 
    color: var(--primary-blue); 
    font-size: 22px; 
    margin: 0;
    font-weight: 700;
}
.logo-text span { color: var(--accent-gold); }

.nav-links {
    display: flex;
    align-items: center;
}
.nav-links a { 
    color: var(--primary-blue); 
    margin-left: 25px; 
    font-weight: 600; 
    text-decoration: none;
    font-size: 14px;
    transition: color 0.3s;
}
.nav-links a:hover { color: var(--accent-gold); }

.btn-login {
    background: var(--primary-blue);
    color: var(--text-light) !important;
    padding: 10px 24px;
    border-radius: 30px;
    font-weight: 700;
    border: 2px solid transparent;
}
.btn-login:hover {
    background: transparent;
    color: var(--primary-blue) !important;
    border: 2px solid var(--primary-blue);
}
"""

html_nav = """
    <div class="top-bar">
        <span>San Joaquín de Turmero</span>
        <span>San Antonio de los Altos</span>
        <span>San Fernando de Apure</span>
        <span>Puerto Ordaz</span>
    </div>

    <nav class="landing-navbar">
        <div class="logo">
            <div class="logo-shield">UBA</div>
            <div class="logo-text">
                <h2>UBA <span>ViveTalentos</span></h2>
            </div>
        </div>
        <div class="nav-links">
            <a href="index.html">Inicio</a>
            <a href="carreras.html">Carreras</a>
            <a href="aliados.html">Empresas</a>
            <a href="dashboard.html" class="btn-login">Mi Plataforma</a>
        </div>
    </nav>
"""

# Modify styles.css
with open("styles.css", "r", encoding="utf-8") as f:
    css_content = f.read()

css_content = re.sub(r'\.main-content\s*{[^}]*}', '.main-content {\n    width: 100%;\n    padding: 30px 5%;\n    min-height: 100vh;\n}', css_content, flags=re.DOTALL)
if "--primary-blue" not in css_content:
    css_content = css_content.replace(":root {", ":root {\n    --primary-blue: #002b5e;\n    --secondary-blue: #004488;\n    --accent-gold: #c99a2e;\n    --text-dark: #1a1a1a;\n    --text-light: #ffffff;\n    --bg-light: #f8f9fa;")

css_content += "\n" + css_to_add

with open("styles.css", "w", encoding="utf-8") as f:
    f.write(css_content)

# Modify HTML files
files = [f for f in os.listdir() if f.endswith('.html')]
for file in files:
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Remove old layout items
    content = re.sub(r'<aside class="sidebar">.*?</aside>', '', content, flags=re.DOTALL)
    content = re.sub(r'<header class="topbar">.*?</header>', '', content, flags=re.DOTALL)
    content = re.sub(r'<div class="top-bar">.*?</div>', '', content, flags=re.DOTALL)
    content = re.sub(r'<nav class="landing-navbar">.*?</nav>', '', content, flags=re.DOTALL)
    
    # Insert new nav right after <body>
    content = re.sub(r'<body[^>]*>', lambda m: m.group(0) + '\n' + html_nav, content)
    
    # In index.html, remove the inline CSS block for the top-bar and landing-navbar
    if file == "index.html":
        content = re.sub(r'/\*\s*Top Bar\s*\*/.*?(?=\/\*\s*Hero Section\s*\*\/)', '', content, flags=re.DOTALL)
    
    with open(file, "w", encoding="utf-8") as f:
        f.write(content)

print("Actualización completada en", len(files), "archivos HTML.")
