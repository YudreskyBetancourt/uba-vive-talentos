with open('styles.css', 'r', encoding='utf-8') as f:
    content = f.read()

bad_css = '''.mobile-toggle-btn {
        display: block;
        color: var(--primary-blue);
        margin-right: 15px;
    }'''

good_css = '''.mobile-toggle-btn {
        display: block;
        color: white; /* Blanco para modo claro */
        margin-right: 15px;
    }'''

if bad_css in content:
    content = content.replace(bad_css, good_css)
    with open('styles.css', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Mobile icon updated successfully")
else:
    print("Mobile icon block not found")
