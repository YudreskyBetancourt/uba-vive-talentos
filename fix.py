with open('dashboard.html', 'r', encoding='utf-8') as f:
    content = f.read()

bad_string = '''            <div style="display: grid; grid-template-columns: 2fr 1fr; gap: 30px; margin-bottom: 40px;">
            
            <div class="card-section">
                <h3 class="card-title">Visibilidad y Métricas Mensuales</h3>
                <canvas id="viewsChart" width="400" height="150"></canvas>
            </div>
        </section>'''

correct_string = '''        <div style="display: grid; grid-template-columns: 2fr 1fr; gap: 30px; margin-bottom: 40px;">
            
            <div class="card-section">
                <h3 class="card-title">Visibilidad y Métricas Mensuales</h3>
                <canvas id="viewsChart" width="400" height="150"></canvas>
            </div>
        </div>
        </section>'''

if bad_string in content:
    content = content.replace(bad_string, correct_string)
    with open('dashboard.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print('Fixed chart section')
else:
    print('Bad string not found')
