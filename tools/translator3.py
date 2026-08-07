import json
from bs4 import BeautifulSoup

with open('Group tour Sinhala.html', 'r', encoding='utf-8') as f:
    html = f.read()

start = html.find('// /* STATE_START */')
end = html.find('// /* STATE_END */')
state_str = html[start + len('// /* STATE_START */\n                const state = reactive(') : end - len(');\n                ')]
current_state = json.loads(state_str)

# Exact matching strings
translations = {
    # Day 2
    "• At පතායා ටයිගර් පාර්ක්, you can view and observe different types of tigers including giant Bengal tigers in a safe and we’ll-managed environment.": "• පතායා ටයිගර් පාර්ක් හිදී, ඔබට ආරක්ෂිත සහ මනාව කළමනාකරණය කළ පරිසරයක් තුළ යෝධ බෙංගාල කොටින් ඇතුළු විවිධ වර්ගයේ කොටින් නැරඹීමට සහ නිරීක්ෂණය කිරීමට හැකිය.",
    "09:00 AM": "පෙ.ව. 09:00",
    
    # Day 3
    "පතායා හෝටලයෙන් පිටවීම (Check-out).": "පතායා හෝටලයෙන් පිටවීම (Check-out).", # wait, I will translate check-out and check-in just in case
    "(Check-out)": "(පිටවීම)",
    "(Check-in)": "(ඇතුළත් වීම)",
    "Picnic Hotel Bangkok 3*": "Picnic Hotel Bangkok (තරු 3)",
    "05:00 PM": "ප.ව. 05:00",
    "05:00 PM ": "ප.ව. 05:00 ",

    # Day 4
    "09:00AM": "පෙ.ව. 09:00",
    " 09:00AM": " පෙ.ව. 09:00",
    "04:00 PM": "ප.ව. 04:00",
}

def translate_html(html_str):
    if not html_str: return html_str
    
    soup = BeautifulSoup(html_str, 'html.parser')
    for text_node in soup.find_all(string=True):
        original = text_node.string
        if not original: continue
        
        # Iterative substring replacement
        for eng, sin in translations.items():
            if eng in original:
                original = original.replace(eng, sin)
        
        if text_node.string != original:
            text_node.replace_with(original)
    
    return str(soup)

for day in current_state.get('days', []):
    desc = day.get('description', '')
    day['description'] = translate_html(desc)

state_json_str = json.dumps(current_state, indent=4, ensure_ascii=False)
new_state_block = '// /* STATE_START */\n                const state = reactive(' + state_json_str + ');\n                '
html = html[:start] + new_state_block + html[end:]

with open('Group tour Sinhala.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Done final replacements.')
