import re
with open('group_tour_builder.html', 'r', encoding='utf8') as f:
    text = f.read()
    matches = re.finditer(r'<[^>]*contenteditable="true"[^>]*>.*?</[^>]+>', text, re.DOTALL)
    for i, m in enumerate(matches):
        print(f'Match {i+1}: {m.group(0)[:100]}...')
