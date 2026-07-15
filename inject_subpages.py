import os
import glob
import re

files = glob.glob('*.html')
for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'class="sidebar"' in content and 'mobile-toggle-btn' not in content:
        if 'Aliado' in content or 'Empresa' in content or 'aliado' in file.lower() or 'empresa' in file.lower():
            text = 'UBA ViveTalentos - Ecosistema Corporativo'
        elif 'Jurado' in content or 'jurado' in file.lower():
            text = 'UBA ViveTalentos - Ecosistema Académico'
        else:
            text = 'San Joaquín de Turmero'
            
        new_topbar = f'''<div class="top-bar">
        <button class="mobile-toggle-btn" id="mobileToggleBtn"><i class="fa-solid fa-bars"></i></button>
        <span>{text}</span>
        
        <div class="top-bar-controls">
            <button class="control-btn" id="darkModeToggle" title="Modo Oscuro/Claro">
                <i class="fa-solid fa-moon" id="darkModeIcon"></i>
            </button>
            <div style="position: relative;">
                <button class="control-btn" id="notifToggle" title="Notificaciones">
                    <i class="fa-solid fa-bell"></i>
                    <span class="notif-badge" id="notifBadge">1</span>
                </button>
                
                <div class="notification-panel" id="notifPanel">
                    <div class="notif-header">Notificaciones</div>
                    <div class="notif-body">
                        <a href="#" class="notif-item">
                            <div class="notif-icon"><i class="fa-solid fa-info-circle"></i></div>
                            <div class="notif-content">
                                <h4>Sistema</h4>
                                <p>Bienvenido a la plataforma UBA ViveTalentos.</p>
                            </div>
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </div>'''
        
        content = re.sub(r'<div class="top-bar">.*?</div>', new_topbar, content, flags=re.DOTALL)
        
        if 'app.js' not in content:
            content = content.replace('</body>', '    <script src="app.js"></script>\n</body>')
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Injected interactive top-bar and app.js into {file}")

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

responsive_css = '''
    /* Fixing small inputs and form rows on mobile */
    .form-row, .profile-contact, .profile-stats-row {
        flex-direction: column !important;
        gap: 15px !important;
    }
    .corp-header, .eval-header {
        flex-direction: column !important;
        text-align: center;
    }
    .search-bar {
        flex-wrap: wrap !important;
        border-radius: 12px !important;
    }
    .search-input {
        width: 100% !important;
        margin-bottom: 10px;
    }
    .btn-filter {
        width: 100%;
        justify-content: center;
    }
    div[style*="display: grid; grid-template-columns: 1fr 2fr;"] {
        display: flex !important;
        flex-direction: column !important;
    }
    div[style*="display: grid; grid-template-columns: 2fr 1fr;"] {
        display: flex !important;
        flex-direction: column-reverse !important; /* Put main content above side panel on mobile */
    }
    div[style*="display: grid;"] {
        grid-template-columns: 1fr !important; /* Catch any remaining inline grids */
    }
'''

if '/* Fixing small inputs and form rows on mobile */' not in css:
    css = re.sub(r'(@media\s*\(max-width:\s*992px\)\s*{)', r'\1\n' + responsive_css, css)
    with open('styles.css', 'w', encoding='utf-8') as f:
        f.write(css)
    print("Added responsive CSS rules")

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    content = content.replace('styles.css?v=4', 'styles.css?v=5')
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
print("Cache updated to v5")
