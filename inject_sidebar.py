import re

files = ['dashboard.html', 'perfil.html']

sidebar_html = """
    <aside class="sidebar">
        <div class="logo-container">
            <i class="fa-solid fa-graduation-cap"></i>
            <h2>UBA <span>ViveTalentos</span></h2>
        </div>
        
        <nav class="nav-menu">
            <a href="index.html" style="margin-bottom: 15px; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 15px;"><i class="fa-solid fa-house"></i> Volver al Inicio</a>

            <a href="dashboard.html" class="[DASH_ACTIVE]"><i class="fa-solid fa-chart-pie"></i> Mi Portafolio</a>
            <a href="#"><i class="fa-solid fa-rocket"></i> Retos Académicos</a>
            <a href="#"><i class="fa-solid fa-handshake"></i> Aliados Comerciales</a>
            <a href="perfil.html" class="[PERF_ACTIVE]"><i class="fa-solid fa-user"></i> Mi Perfil</a>
            
            <a href="login.html" style="margin-top: auto; color: #f87171;"><i class="fa-solid fa-right-from-bracket"></i> Cerrar Sesión</a>
        </nav>
    </aside>
"""

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if already has sidebar to avoid duplicates
    if '<aside class="sidebar">' in content:
        content = re.sub(r'<aside class="sidebar">.*?</aside>', '', content, flags=re.DOTALL)
    
    # Add has-sidebar to body
    content = re.sub(r'<body[^>]*>', r'<body class="has-sidebar">', content)
    
    # Prepare correct active class
    s = sidebar_html
    if file == 'dashboard.html':
        s = s.replace('[DASH_ACTIVE]', 'activo').replace('[PERF_ACTIVE]', '')
    else:
        s = s.replace('[DASH_ACTIVE]', '').replace('[PERF_ACTIVE]', 'activo')
        
    # Insert sidebar right after body
    content = re.sub(r'(<body class="has-sidebar">)', r'\1' + '\n' + s, content)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Actualizados dashboard y perfil")
