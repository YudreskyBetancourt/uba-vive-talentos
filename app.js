// app.js - Script central de funcionalidades interactivas (Fase WOW)

document.addEventListener('DOMContentLoaded', () => {
    
    // 1. INICIALIZAR MODO OSCURO (DARK MODE)
    const darkModeToggle = document.getElementById('darkModeToggle');
    const darkModeIcon = document.getElementById('darkModeIcon');
    
    // Verificar si el usuario ya tenía el modo oscuro activo en localStorage
    if (localStorage.getItem('uba_dark_mode') === 'true') {
        document.body.classList.add('dark-mode');
        if(darkModeIcon) {
            darkModeIcon.classList.replace('fa-moon', 'fa-sun');
        }
    }

    if (darkModeToggle) {
        darkModeToggle.addEventListener('click', () => {
            document.body.classList.toggle('dark-mode');
            
            const isDark = document.body.classList.contains('dark-mode');
            localStorage.setItem('uba_dark_mode', isDark);

            if (isDark) {
                darkModeIcon.classList.replace('fa-moon', 'fa-sun');
            } else {
                darkModeIcon.classList.replace('fa-sun', 'fa-moon');
            }
        });
    }

    // 2. TOGGLE DE NOTIFICACIONES
    const notifToggle = document.getElementById('notifToggle');
    const notifPanel = document.getElementById('notifPanel');
    const notifBadge = document.getElementById('notifBadge');

    if (notifToggle && notifPanel) {
        notifToggle.addEventListener('click', (e) => {
            e.stopPropagation();
            notifPanel.classList.toggle('active');
            
            // Si el usuario abre las notificaciones, quitamos el badge rojo (simula que ya las vio)
            if (notifBadge && notifPanel.classList.contains('active')) {
                notifBadge.style.display = 'none';
            }
        });

        // Cerrar panel al hacer clic fuera
        document.addEventListener('click', (e) => {
            if (!notifPanel.contains(e.target) && !notifToggle.contains(e.target)) {
                notifPanel.classList.remove('active');
            }
        });
    }

    // 3. RESPONSIVE SIDEBAR (Menú Hamburguesa)
    const mobileToggleBtn = document.getElementById('mobileToggleBtn');
    const sidebar = document.querySelector('.sidebar');
    
    if (mobileToggleBtn && sidebar) {
        // Crear el overlay dinámicamente
        const overlay = document.createElement('div');
        overlay.classList.add('sidebar-overlay');
        document.body.appendChild(overlay);

        mobileToggleBtn.addEventListener('click', () => {
            sidebar.classList.add('open');
            overlay.classList.add('active');
        });

        // Cerrar sidebar al hacer clic en el overlay (fuera del sidebar)
        overlay.addEventListener('click', () => {
            sidebar.classList.remove('open');
            overlay.classList.remove('active');
        });
    }

});

// 4. SIMULADOR DE INTELIGENCIA ARTIFICIAL (Para el Perfil)
function enhanceBioWithAI() {
    const aiBtn = document.getElementById('aiEnhanceBtn');
    const aiLoading = document.getElementById('aiLoading');
    const bioTextarea = document.getElementById('bioTextarea');

    if(!bioTextarea) return;

    // Cambiar estado visual
    aiBtn.style.display = 'none';
    aiLoading.style.display = 'flex';

    // Simular tiempo de carga (2.5 segundos)
    setTimeout(() => {
        // Ocultar carga y mostrar botón
        aiLoading.style.display = 'none';
        aiBtn.style.display = 'inline-flex';
        aiBtn.innerHTML = '<i class="fa-solid fa-check"></i> Biografía Optimizada';
        aiBtn.style.background = '#10B981'; // Color verde de éxito
        aiBtn.style.boxShadow = 'none';

        // Reemplazar texto por uno más "Profesional"
        const improvedBio = "Comunicadora Social especializada en narrativas digitales y producción audiovisual multiplataforma. Combino visión creativa con pensamiento estratégico para diseñar campañas de alto impacto. Demostrada capacidad de adaptación en equipos multidisciplinarios y firme compromiso con la creación de contenidos de valor social.";
        
        bioTextarea.value = improvedBio;
        
        // Animación de destello dorado
        bioTextarea.style.boxShadow = '0 0 0 3px rgba(139, 92, 246, 0.4)';
        setTimeout(() => { bioTextarea.style.boxShadow = 'none'; }, 1000);
        
    }, 2500);
}
