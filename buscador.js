document.addEventListener("DOMContentLoaded", function() {
    const globalSearch = document.getElementById('global-search');
    const resultsContainer = document.getElementById('global-search-results');

    // Base de datos de navegación rápida
    const links = [
        { nombre: "Comunicación Social", url: "carreras.html" },
        { nombre: "Derecho", url: "carreras.html" },
        { nombre: "Simulacros y Retos", url: "retos.html" },
        { nombre: "Empresas Aliadas", url: "aliados.html" },
        { nombre: "Mi Perfil", url: "perfil.html" }
    ];

    if (globalSearch) {
        globalSearch.addEventListener('input', function() {
            const query = this.value.toLowerCase();
            
            // Si el contenedor de resultados no existe, créalo dinámicamente
            if (!resultsContainer) {
                const newResults = document.createElement('div');
                newResults.id = 'global-search-results';
                newResults.className = 'search-results';
                globalSearch.parentNode.appendChild(newResults);
            }

            const results = document.getElementById('global-search-results');
            results.innerHTML = '';

            if (query.length > 0) {
                const filtered = links.filter(l => l.nombre.toLowerCase().includes(query));
                filtered.forEach(item => {
                    results.innerHTML += `<a href="${item.url}" class="search-item">${item.nombre}</a>`;
                });
                results.classList.add('active');
            } else {
                results.classList.remove('active');
            }
        });
    }
});
