with open('styles.css', 'r', encoding='utf-8') as f:
    content = f.read()

bad_css = '''.control-btn {
    background: transparent;
    border: none;
    font-size: 18px;
    color: var(--primary-blue);
    cursor: pointer;
    position: relative;
    transition: 0.3s;
}'''

good_css = '''.control-btn {
    background: transparent;
    border: none;
    font-size: 18px;
    color: white; /* Cambiado a blanco para modo claro */
    cursor: pointer;
    position: relative;
    transition: 0.3s;
}'''

if bad_css in content:
    content = content.replace(bad_css, good_css)
    with open('styles.css', 'w', encoding='utf-8') as f:
        f.write(content)
    print("CSS updated successfully")
else:
    print("CSS block not found")
