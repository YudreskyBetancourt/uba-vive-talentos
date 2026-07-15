with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

bad_css_hero = '.profile-hero { flex-direction: column; text-align: center; }'
good_css_hero = '.profile-hero { flex-direction: column !important; text-align: center !important; }'
css = css.replace(bad_css_hero, good_css_hero)

bad_css_stats = '.profile-stats-row { position: relative; top: auto; right: auto; margin-top: 20px; justify-content: center; }'
good_css_stats = '.profile-stats-row { position: relative !important; top: auto !important; right: auto !important; margin-top: 20px !important; justify-content: center !important; flex-direction: column !important; }'
css = css.replace(bad_css_stats, good_css_stats)

bad_css_info = '.profile-info h1 { justify-content: center; }'
good_css_info = '.profile-info h1 { justify-content: center !important; }'
css = css.replace(bad_css_info, good_css_info)

bad_css_contact = '.profile-contact { justify-content: center; flex-wrap: wrap; }'
good_css_contact = '.profile-contact { justify-content: center !important; flex-wrap: wrap !important; flex-direction: column !important; }'
css = css.replace(bad_css_contact, good_css_contact)

bad_css_tabs = '.profile-tabs { flex-wrap: wrap; justify-content: center; }'
good_css_tabs = '.profile-tabs { flex-wrap: wrap !important; justify-content: center !important; }'
css = css.replace(bad_css_tabs, good_css_tabs)

bad_css_layout = '.profile-grid-layout { grid-template-columns: 1fr; }'
good_css_layout = '.profile-grid-layout { grid-template-columns: 1fr !important; }'
css = css.replace(bad_css_layout, good_css_layout)

# And what about the chart.js canvas?
if '.chart-container' not in css:
    css = css.replace('} /* end of media query */', '') # I can just append it inside the media query
    import re
    css = re.sub(r'}\s*@keyframes slideDownFade', r'    .chart-container { width: 100% !important; overflow-x: auto; }\n}\n\n@keyframes slideDownFade', css)

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)

print('Fixed CSS !important rules')
