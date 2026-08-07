import json
from bs4 import BeautifulSoup

with open('state_eng.json', encoding='utf-8') as f:
    state = json.load(f)

# Using exact nodes found in HTML
translations = {
    # Day 2
    "Coral Island Tour by Speed Boat with Lunch": "දිවා ආහාරය සමඟ ස්පීඩ් බෝට්ටුවකින් කොරල් දූපත් චාරිකාව",
    " We will pick you up from your Pattaya hotel around ": " උදෑසන 09:00 ට පමණ පතායා හෝටලයෙන් ඔබව රැගෙන ගමන් ආරම්භ කරයි. ",
    " and transfer will begin. You will travel to Coral Island by speedboat.": " ඔබ ස්පීඩ් බෝට්ටුවකින් කොරල් දූපත වෙත ගමන් කරනු ඇත.",
    " On the way, you can experience parasailing, jet skiing, and an under water walk (": " අතරමගදී, ඔබට පැරසේලිං, ජෙට් ස්කීං සහ දිය යට ඇවිදීම අත්විඳිය හැකිය (",
    "These activities are not included in the package": "මේවා පැකේජයට ඇතුළත් නොවේ",
    " Lunch will be served at an Indian restaurant.": " ඉන්දියානු ආපනශාලාවකදී දිවා ආහාරය පිරිනමනු ලැබේ.",
    " (Lunch will be provided by the Coral Island boat company as a complimentary.)": " (දිවා ආහාරය කොරල් දූපත් බෝට්ටු සමාගම විසින් නොමිලේ සපයනු ලැබේ.)",
    " At Pattaya Tiger Park, you can view and observe different types of tigers including giant Bengal tigers in a safe and well-managed environment.": " පතායා ටයිගර් පාර්ක් හිදී, ඔබට ආරක්ෂිත සහ මනාව කළමනාකරණය කළ පරිසරයක් තුළ යෝධ බෙංගාල කොටින් ඇතුළු විවිධ වර්ගයේ කොටින් නැරඹීමට සහ නිරීක්ෂණය කිරීමට හැකිය.",
    " Optional-You can choose to go in the cage (10-15 mins.) to feel, touch, hug and play with tigers.Also you can take pictures with tigers. (": " විකල්ප - කොටින් දැනීමට, ස්පර්ශ කිරීමට, බදා ගැනීමට සහ සෙල්ලම් කිරීමට කූඩුවට යාමට (විනාඩි 10-15) ඔබට තෝරා ගත හැකිය. තවද ඔබට කොටින් සමඟ ඡායාරූප ගත හැකිය. (",
    "Pattaya Tiger Park": "පතායා ටයිගර් පාර්ක්",
    "Breakfast at Hotel": "හෝටලයෙන් උදෑසන ආහාරය",

    # Day 3
    " After breakfast\xa0 Morning\xa0": " උදෑසන ආහාරයෙන් පසු, උදෑසන ",
    "check out from Pattaya hotel.": "පතායා හෝටලයෙන් පිටවීම (Check-out).",
    " You will be picked up from Pattaya Hotel &transferred to Bangkok": " පතායා හෝටලයෙන් ඔබව රැගෙන බැංකොක් වෙත ගමන් කරයි",
    "Sea life Bangkok Ocean World + Madame Tussauds Wax museum": "සී ලයිෆ් බැංකොක් ඕෂන් වර්ල්ඩ් + මැඩම් ටුසාඩ්ස් ඉටි රූප කෞතුකාගාරය",
    " Experience a fun-filled day in Bangkok with visits to SEA LIFE Bangkok Ocean World and Madame Tussauds Bangkok.\xa0": " සී ලයිෆ් බැංකොක් ඕෂන් වර්ල්ඩ් සහ මැඩම් ටුසාඩ්ස් බැංකොක් නැරඹීම සමඟ බැංකොක් නුවර විනෝදයෙන් පිරි දවසක් අත්විඳින්න. ",
    " Discover fascinating marine life and walk through an exciting under water tunnel before enjoying interactive moments and photo opportunities with life like celebrity figures perfect for a memorable and entertaining city experience.": " සිත් ඇදගන්නාසුළු සාගර ජීවීන් සොයාගෙන ආකර්ෂණීය දිය යට උමඟක් හරහා ඇවිදින්න. ඉන්පසු ලොව ප්‍රසිද්ධ පුද්ගලයින්ගේ සැබෑවටම සමාන ඉටි රූප සමඟ අන්තර්ක්‍රියාකාරී අවස්ථා සහ ඡායාරූප ගැනීමේ අවස්ථා භුක්ති විඳින්න. මෙය අමතක නොවන නගර අත්දැකීමක් වනු ඇත.",
    " After the tour, you will be transferred to the Picnic 3* Hotel in Bangkok.": " චාරිකාවෙන් පසු, ඔබව බැංකොක් හි පික්නික් හෝටලය (තරු 3) වෙත ගෙන යනු ඇත.",
    " Check in at 02.00pm to ": " ප.ව. 02.00 ට හෝටලයට ඇතුළත් වීම (Check-in) - ",
    "Picnic HotelBangkok3*": "Picnic Hotel Bangkok 3*",
    "Chao Phraya Cruise Dinner": "චාඕ ෆ්‍රායා කෲස් රාත්‍රී ආහාරය",
    " Get ready to be picked up at ": " ප.ව. 05:00 ට සූදානම් වන්න! ",
    "for a magical evening on the Chao Phraya Dinner Cruise! Experience serene river cruise encompassing rich Thai royal history.\xa0": "චාඕ ෆ්‍රායා රාත්‍රී ආහාර කෲස් එකේ අපූරු සන්ධ්‍යාවක් සඳහා! පොහොසත් තායි රාජකීය ඉතිහාසය වටා ගෙතුණු සන්සුන් ගංගා චාරිකාවක් අත්විඳින්න. ",
    " Splendid illumination of Bangkok landmarks under neon lights.": " නියොන් ආලෝකය යටතේ බැංකොක් හි සන්ධිස්ථානවල අලංකාර ආලෝකකරණය.",
    " Delicious & tasty buffet with international delicacies": " ජාත්‍යන්තර ප්‍රණීත ආහාර සහිත රසවත් බුෆේ",

    # Day 4
    "After enjoying your breakfast, get ready for a": "උදෑසන ආහාරය භුක්ති විඳීමෙන් පසු,",
    " pickup from the hotel for a fun-filled day at Dream World & Snow Town!": " ට හෝටලයෙන් පිටත් වීමට සූදානම් වන්න ඩ්‍රීම් වර්ල්ඩ් සහ ස්නෝ ටවුන් හි විනෝදයෙන් පිරි දවසක් සඳහා!",
    "Dream World & Snow Town with Lunch": "දිවා ආහාරය සමඟ ඩ්‍රීම් වර්ල්ඩ් සහ ස්නෝ ටවුන්",
    " Dream World & Snow Town has been a popular amusement park in Thailand for locals and tourists alike for many years.\xa0": " ඩ්‍රීම් වර්ල්ඩ් සහ ස්නෝ ටවුන් වසර ගණනාවක් පුරා ප්‍රදේශවාසීන් සහ සංචාරකයින් අතර තායිලන්තයේ ජනප්‍රිය විනෝද උද්‍යානයක් විය. ",
    " Whether you are a fan of adventure activities or thrill rides, Dream World & Snow Town will be a definite hit no matter your age!": " ඔබ ත්‍රාසජනක ක්‍රියාකාරකම් වලට හෝ සවාරි වලට කැමති අයෙකු වුවද, ඔබේ වයස කුමක් වුවත් ඩ්‍රීම් වර්ල්ඩ් සහ ස්නෝ ටවුන් ඔබට අනිවාර්යයෙන්ම ගැලපෙනු ඇත!",
    ", we will depart from Dream World.": " ට පමණ අපි ඩ්‍රීම් වර්ල්ඩ් වෙතින් පිටත් වෙමු.",
    " Around ": " ප.ව. ",

    # Day 5
    " Youre free to relaxing or shopping to your satisfaction": " ඔබට විවේක ගැනීමට හෝ ඔබේ සිතැඟි පරිදි සාප්පු සවාරි යාමට නිදහස ඇත",
    " Youll have free time to explore popular shopping locations like Platinum Mall, Indra Market, Big C, Palladium Mall, Central World, and more. Dont worry well walk you to all the best spots!\xa0": " Platinum Mall, Indra Market, Big C, Palladium Mall, Central World වැනි ජනප්‍රිය සාප්පු සවාරි ස්ථාන ගවේෂණය කිරීමට ඔබට නිදහස් කාලය ලැබෙනු ඇත. බිය නොවන්න, අපි ඔබව හොඳම ස්ථාන වලට මඟ පෙන්වන්නෙමු! ",
    " Your Bangkok hotel is within walking distance of shopping malls.\xa0": " ඔබේ බැංකොක් හෝටලය සාප්පු සංකීර්ණ වලට ඇවිද යා හැකි දුරකින් පිහිටා ඇත. ",
    
    # Common
    "Sightseeing": "දර්ශන නැරඹීම",
    "Tours": "චාරිකා",
    "Overnight Stay at Hotel": "රාත්‍රිය හෝටලයේ ගත කිරීම",
}

def translate_html(html_str):
    if not html_str: return html_str
    
    # Pre-clean smart quotes replaced by question marks in utf8 to ascii issue
    html_str = html_str.replace("Youre", "You’re")
    html_str = html_str.replace("Youll", "You’ll")
    html_str = html_str.replace("Dont", "Don’t")
    html_str = html_str.replace("well", "we’ll")
    
    # Also fix translations dict for these
    translations[" You’re free to relaxing or shopping to your satisfaction"] = " ඔබට විවේක ගැනීමට හෝ ඔබේ සිතැඟි පරිදි සාප්පු සවාරි යාමට නිදහස ඇත"
    translations[" You’ll have free time to explore popular shopping locations like Platinum Mall, Indra Market, Big C, Palladium Mall, Central World, and more. Don’t worry we’ll walk you to all the best spots!\xa0"] = " Platinum Mall, Indra Market, Big C, Palladium Mall, Central World වැනි ජනප්‍රිය සාප්පු සවාරි ස්ථාන ගවේෂණය කිරීමට ඔබට නිදහස් කාලය ලැබෙනු ඇත. බිය නොවන්න, අපි ඔබව හොඳම ස්ථාන වලට මඟ පෙන්වන්නෙමු! "

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

with open('Group tour Sinhala.html', 'r', encoding='utf-8') as f:
    html = f.read()

start = html.find('// /* STATE_START */')
end = html.find('// /* STATE_END */')

# We'll pull the state string from the file, decode it, apply translation, and encode it back.
state_str = html[start + len('// /* STATE_START */\n                const state = reactive(') : end - len(');\n                ')]
current_state = json.loads(state_str)

for day in current_state.get('days', []):
    desc = day.get('description', '')
    day['description'] = translate_html(desc)

state_json_str = json.dumps(current_state, indent=4, ensure_ascii=False)
new_state_block = '// /* STATE_START */\n                const state = reactive(' + state_json_str + ');\n                '
html = html[:start] + new_state_block + html[end:]

with open('Group tour Sinhala.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Done fixing days 2 to 5 exactly.')
