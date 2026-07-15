import os
import re
import unicodedata

def slugify(value):
    value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    value = re.sub(r'[^\w\s-]', '', value).strip().lower()
    return re.sub(r'[-\s]+', '-', value)

TEMPLATE = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Perfil de {company_name} - UBA Vive Talentos</title>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@600;700;800&family=Open+Sans:wght@400;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link rel="stylesheet" href="styles.css">
    <style>
        .company-cover {{
            height: 250px;
            background-image: linear-gradient(to top, rgba(0,26,56,0.9), rgba(0,43,94,0.3)), url('https://images.unsplash.com/photo-1497215728101-856f4ea42174?auto=format&fit=crop&q=80&w=1200');
            background-size: cover;
            background-position: center;
            border-radius: 16px 16px 0 0;
            position: relative;
        }}
        
        .company-profile-header {{
            background: var(--blanco);
            padding: 0 40px 30px 40px;
            border-radius: 0 0 16px 16px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.05);
            margin-bottom: 40px;
            display: flex;
            align-items: flex-end;
            justify-content: space-between;
            position: relative;
        }}

        .cp-logo-container {{
            margin-top: -60px;
            display: flex;
            align-items: flex-end;
            gap: 20px;
        }}

        .cp-logo {{
            width: 120px;
            height: 120px;
            border-radius: 20px;
            display: flex;
            justify-content: center;
            align-items: center;
            font-size: 45px;
            font-weight: 800;
            color: white;
            border: 5px solid var(--blanco);
            box-shadow: 0 10px 20px rgba(0,0,0,0.1);
            background: {company_color};
        }}

        .cp-info h1 {{
            font-size: 32px;
            color: var(--primary-blue);
            margin-bottom: 5px;
        }}

        .cp-info p {{
            font-size: 16px;
            color: var(--gris-texto);
            font-weight: 600;
        }}

        .btn-follow {{
            background: var(--primary-blue);
            color: white;
            padding: 12px 30px;
            border: none;
            border-radius: 8px;
            font-weight: 700;
            font-size: 15px;
            cursor: pointer;
            transition: 0.3s;
            display: flex;
            align-items: center;
            gap: 8px;
        }}

        .btn-follow:hover {{
            background: var(--accent-gold);
            color: var(--primary-blue);
        }}

        .cp-content-grid {{
            display: grid;
            grid-template-columns: 2fr 1fr;
            gap: 30px;
            margin-bottom: 50px;
        }}

        .cp-card {{
            background: var(--blanco);
            border-radius: 16px;
            padding: 30px;
            box-shadow: 0 5px 20px rgba(0,0,0,0.05);
            border: 1px solid var(--gris-claro);
            margin-bottom: 30px;
        }}

        .cp-card h3 {{
            font-size: 20px;
            color: var(--primary-blue);
            margin-bottom: 20px;
            display: flex;
            align-items: center;
            gap: 10px;
            border-bottom: 2px solid var(--gris-fondo);
            padding-bottom: 10px;
        }}

        .cp-about {{
            font-size: 15px;
            color: var(--gris-texto);
            line-height: 1.7;
        }}

        /* Styles for the injected vacancies */
        .vacancy-item {{
            background: var(--blanco);
            border: 1px solid #E2E8F0;
            border-radius: 8px;
            padding: 15px;
            margin-bottom: 15px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}
        .vac-title {{
            font-size: 15px;
            font-weight: 700;
            color: var(--text-dark);
            margin-bottom: 8px;
        }}
        .vac-details {{
            display: flex;
            gap: 15px;
            font-size: 13px;
            color: var(--gris-texto);
            font-weight: 600;
        }}
        .vac-salary {{
            color: var(--verde-exito);
            background: #D1FAE5;
            padding: 4px 8px;
            border-radius: 4px;
        }}
        .btn-apply {{
            background: transparent;
            border: 2px solid var(--primary-blue);
            color: var(--primary-blue);
            padding: 8px 20px;
            border-radius: 8px;
            font-weight: 700;
            cursor: pointer;
            transition: 0.3s;
        }}
        .btn-apply:hover {{
            background: var(--primary-blue);
            color: white;
        }}
    </style>
</head>
<body class="has-sidebar">

    <aside class="sidebar">
        <div class="logo-container">
            <i class="fa-solid fa-graduation-cap"></i>
            <h2>UBA <span>ViveTalentos</span></h2>
        </div>
        
        <nav class="nav-menu">
            <a href="index.html" style="margin-bottom: 15px; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 15px;"><i class="fa-solid fa-house"></i> Volver al Inicio</a>

            <a href="dashboard.html"><i class="fa-solid fa-chart-pie"></i> Mi Portafolio</a>
            <a href="retos.html"><i class="fa-solid fa-rocket"></i> Retos Académicos</a>
            <a href="aliados.html" class="activo"><i class="fa-solid fa-handshake"></i> Aliados Comerciales</a>
            <a href="perfil.html"><i class="fa-solid fa-user"></i> Mi Perfil</a>
            
            <a href="login.html" style="margin-top: auto; color: #f87171;"><i class="fa-solid fa-right-from-bracket"></i> Cerrar Sesión</a>
        </nav>
    </aside>

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
            <a href="aliados.html" class="btn-login" style="background: transparent; color: var(--primary-blue); border: none; font-weight: 600;">Empresas</a>
        </div>
    </nav>

    <main class="main-content">
        
        <!-- Volver -->
        <a href="aliados.html" style="display: inline-block; margin-bottom: 20px; color: var(--primary-blue); text-decoration: none; font-weight: 600;"><i class="fa-solid fa-arrow-left"></i> Volver al Directorio</a>

        <!-- Hero de Empresa -->
        <div class="company-cover"></div>
        <div class="company-profile-header">
            <div class="cp-logo-container">
                <div class="cp-logo">{company_logo_text}</div>
                <div class="cp-info">
                    <h1>{company_name} <i class="fa-solid fa-circle-check" style="color: #38A169; font-size: 20px;" title="Empresa Verificada"></i></h1>
                    <p>{company_sector} | Venezuela</p>
                </div>
            </div>
            <button class="btn-follow"><i class="fa-solid fa-plus"></i> Seguir Empresa</button>
        </div>

        <div class="cp-content-grid">
            <!-- Columna Izquierda (Vacantes y Retos) -->
            <div>
                <div class="cp-card">
                    <h3><i class="fa-solid fa-briefcase" style="color: var(--accent-gold);"></i> Vacantes Disponibles</h3>
                    <p style="margin-bottom: 20px; color: var(--gris-texto); font-size: 14px;">Postúlate directamente a las vacantes exclusivas que {company_name} tiene para los estudiantes de la UBA.</p>
                    
                    {vacancies_html}

                </div>

                <div class="cp-card">
                    <h3><i class="fa-solid fa-rocket" style="color: var(--accent-gold);"></i> Retos Activos</h3>
                    <div style="background: #FFFBEB; border: 1px solid #FDE68A; padding: 20px; border-radius: 8px; text-align: center;">
                        <i class="fa-solid fa-ranking-star" style="font-size: 30px; color: #D97706; margin-bottom: 10px;"></i>
                        <h4 style="color: #92400E; margin-bottom: 5px;">¡Aún no hay retos activos!</h4>
                        <p style="color: #B45309; font-size: 13px;">Sigue a la empresa para recibir notificaciones cuando lancen un nuevo reto académico.</p>
                    </div>
                </div>
            </div>

            <!-- Columna Derecha (Nosotros) -->
            <div>
                <div class="cp-card">
                    <h3><i class="fa-solid fa-circle-info" style="color: var(--accent-gold);"></i> Acerca de Nosotros</h3>
                    <p class="cp-about">
                        {company_desc}
                        <br><br>
                        En <strong>{company_name}</strong> valoramos el talento joven, la innovación y el deseo de superar los límites. 
                        Al unirte a nuestro equipo, formarás parte de una cultura que impulsa el crecimiento personal y profesional.
                    </p>
                    
                    <hr style="border: none; border-top: 1px solid var(--gris-fondo); margin: 20px 0;">
                    
                    <h4 style="font-size: 14px; color: var(--text-dark); margin-bottom: 15px;">Información de Contacto</h4>
                    <ul style="list-style: none; padding: 0; margin: 0; font-size: 13px; color: var(--gris-texto); display: flex; flex-direction: column; gap: 10px;">
                        <li><i class="fa-solid fa-globe" style="width: 20px; color: var(--primary-blue);"></i> www.{company_slug}.com.ve</li>
                        <li><i class="fa-solid fa-envelope" style="width: 20px; color: var(--primary-blue);"></i> talento@{company_slug}.com.ve</li>
                        <li><i class="fa-solid fa-location-dot" style="width: 20px; color: var(--primary-blue);"></i> Sede Principal, Venezuela</li>
                    </ul>
                </div>
            </div>
        </div>

    </main>

</body>
</html>
"""

def main():
    filepath = 'aliados.html'
    if not os.path.exists(filepath):
        print("aliados.html no encontrado.")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # Find all company cards
    pattern = r'<div class="company-card">(.*?)<div class="cc-footer">'
    cards = re.findall(pattern, html, re.DOTALL)
    print(f"Encontradas {len(cards)} empresas.")

    updated_html = html

    for card in cards:
        # Extract logo info
        logo_match = re.search(r'<div class="cc-logo" style="background:\s*([^;]+);[^>]*>([^<]+)</div>', card)
        if not logo_match:
            continue
        color = logo_match.group(1)
        logo_text = logo_match.group(2).strip()

        # Extract name and sector
        header_match = re.search(r'<h3>([^<]+)</h3><p>([^<]+)</p>', card)
        if not header_match:
            continue
        name = header_match.group(1).strip()
        sector = header_match.group(2).strip()

        # Extract desc
        desc_match = re.search(r'<div class="cc-body">([^<]+)</div>', card)
        desc = desc_match.group(1).strip() if desc_match else ""

        # Extract vacancies
        vacancies_block = ""
        vac_match = re.search(r'<div class="cc-vacancies">(.*?)</div>', card, re.DOTALL)
        if vac_match:
            vac_inner = vac_match.group(1)
            # Find all vacancy items
            items = re.findall(r'<div class="vacancy-item">(.*?)</div>', vac_inner, re.DOTALL)
            
            for item in items:
                # Add a "Postularme" button to each item for the detailed page
                title_match = re.search(r'<div class="vac-title">([^<]+)</div>', item)
                details_match = re.search(r'<div class="vac-details">(.*?)</div>', item, re.DOTALL)
                if title_match and details_match:
                    vtitle = title_match.group(1)
                    vdetails = details_match.group(1)
                    
                    vacancies_block += f'''
                    <div class="vacancy-item" style="display:flex; justify-content:space-between; align-items:center;">
                        <div>
                            <div class="vac-title">{vtitle}</div>
                            <div class="vac-details">{vdetails}</div>
                        </div>
                        <button class="btn-apply">Postularme</button>
                    </div>
                    '''

        slug = slugify(name)
        file_name = f"empresa-{slug}.html"

        # Generate specific file
        file_content = TEMPLATE.format(
            company_name=name,
            company_color=color,
            company_logo_text=logo_text,
            company_sector=sector,
            company_desc=desc,
            company_slug=slug,
            vacancies_html=vacancies_block
        )

        with open(file_name, 'w', encoding='utf-8') as out:
            out.write(file_content)
        
        print(f"Creado: {file_name}")

        # Replace button in aliados.html
        # We need to find the specific footer for this card.
        # Since we are iterating, it's safer to just replace the whole card block if possible, 
        # but regex might be tricky. Let's do a specific replace.
        
        # original footer button: <button>Ver Perfil Completo</button>
        # we need to replace it just for this company. We can use a regex that includes the company name.
        
        # We'll use a very specific regex to replace the footer button of THIS company card
        card_pattern = r'(<h3>' + re.escape(name) + r'</h3>.*?<div class="cc-footer">)\s*<button>Ver Perfil Completo</button>'
        updated_html = re.sub(card_pattern, r'\1<a href="' + file_name + '" style="display:block; width:100%; background:transparent; color:var(--primary-blue); border:2px solid var(--primary-blue); padding:8px; border-radius:8px; font-weight:700; cursor:pointer; text-align:center; text-decoration:none; box-sizing:border-box;">Ver Perfil Completo</a>', updated_html, flags=re.DOTALL)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(updated_html)
    print("aliados.html actualizado con los enlaces a los perfiles individuales.")

if __name__ == "__main__":
    main()
