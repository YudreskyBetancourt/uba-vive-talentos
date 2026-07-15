with open('dashboard.html', 'r', encoding='utf-8') as f:
    content = f.read()

bad_string = '''                <div class="p-stat-box">
                    <i class="fa-solid fa-eye"></i>
                    <h3>2,845</h3>
                    <p>Visualizaciones</p>
                </div>
        <div style="display: grid; grid-template-columns: 2fr 1fr; gap: 30px; margin-bottom: 40px;">
            
            <div class="card-section">
                <h3 class="card-title">Visibilidad y Métricas Mensuales</h3>
                <canvas id="viewsChart" width="400" height="150"></canvas>
            </div>
        </div>
        </section>'''

correct_string = '''                <div class="p-stat-box">
                    <i class="fa-solid fa-eye"></i>
                    <h3>2,845</h3>
                    <p>Visualizaciones</p>
                </div>
                <div class="p-stat-box">
                    <i class="fa-solid fa-star"></i>
                    <h3>98%</h3>
                    <p>Valoración</p>
                </div>
            </div>
        </section>

        <div style="display: grid; grid-template-columns: 1fr; gap: 30px; margin-bottom: 40px; margin-top: 40px;">
            <div class="card-section">
                <h3 class="card-title">Visibilidad y Métricas Mensuales</h3>
                <canvas id="viewsChart" width="400" height="150"></canvas>
            </div>
        </div>'''

if bad_string in content:
    content = content.replace(bad_string, correct_string)
    
    # Also fix the cache issue
    content = content.replace('href="styles.css"', 'href="styles.css?v=2"')
    
    with open('dashboard.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print('Fixed dashboard layout')
else:
    print('Bad string not found')
