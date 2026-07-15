with open('dashboard.html', 'r', encoding='utf-8') as f:
    content = f.read()

import re
content = re.sub(r'(<canvas id="activityChart".*?</canvas>)', r'<div style="width: 100%; max-width: 100%; overflow-x: auto;">\1</div>', content)

# Remove any stray inline <style> elements that could interfere with mobile queries.
# Wait, let's just make sure we updated styles.css properly with !important

with open('dashboard.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Canvas wrapped')
