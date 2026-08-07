import json
from bs4 import BeautifulSoup

with open('state_eng.json', encoding='utf-8') as f:
    state = json.load(f)

translations = {
    # Day 1
    "Arrival to Bangkok Don Mueang International Airport": "බැංකොක් Don Mueang ජාත්‍යන්තර ගුවන් තොටුපළ වෙත පැමිණීම",
    "On the way to Pattaya there will be a stop for breakfast at": "පතායා වෙත යන අතරමගදී උදෑසන ආහාරය සඳහා නතර වේ",
    "Baiyoke Sky Breakfast": "Baiyoke Sky උදෑසන ආහාරය",
    "Pattaya Big BuddhaTemple Tour": "පතායා බිග් බුද්ධා විහාරස්ථාන චාරිකාව",
    "Afterwards experience a panoramic view of the city and its surroundings from the Birds Eye View.": "ඉන්පසු නගරය සහ අවට ප්‍රදේශයේ දර්ශනයක් කුරුල්ලෙකුගේ ඇසින් (Birds Eye View) නැරඹීමේ අත්දැකීම ලබාගන්න.",
    "Marvel at the sheer size and grandiosity of the Big Buddha Statue at Wat Phra Yai": "Wat Phra Yai හි ඇති බිග් බුද්ධා ප්‍රතිමාවේ විශාලත්වය සහ ශ්‍රේෂ්ඨත්වය දැක බලාගන්න",
    "Pattaya Dolphinarium is widely considered the number 01 marine mammal show in Asia, featuring world-class performances by South American fur seals and bottlenose dolphins.": "පතායා ඩොල්ෆිනාරියම් ආසියාවේ අංක 01 සාගර ක්ෂීරපායී දර්ශනය ලෙස පුළුල්ව සැලකෙන අතර, දකුණු ඇමරිකානු ලොම් සහිත සීල් මත්ස්‍යයින් සහ බොට්ල්නෝස් ඩොල්ෆින්ගේ ලෝක මට්ටමේ ප්‍රසංග වලින් සමන්විත වේ.",
    "Pattaya Dolphinarium": "පතායා ඩොල්ෆිනාරියම්",
    "Intelligent dolphins and charming seals will showcase a range of skills, from impressive acrobatics to heart warming interactions, it will be a truly unforgettable experience for you": "බුද්ධිමත් ඩොල්ෆින් සහ ආකර්ශනීය සීල් මත්ස්‍යයින් විවිධ කුසලතා ප්‍රදර්ශනය කරනු ඇත. විශ්මයජනක ඇක්‍රොබැටික් වල සිට හදවත් උණුසුම් කරන අන්තර්ක්‍රියා දක්වා, එය ඔබට සැබවින්ම අමතක නොවන අත්දැකීමක් වනු ඇත.",
    "After the tour you will be picked up from Pattaya Sightseeing": "චාරිකාවෙන් පසු පතායා නැරඹුම් ප්‍රදේශයෙන් ඔබව රැගෙන",
    "proceed to": "ගමන් කරයි",
    "Baron Beach Hotel Pattaya 3*": "Baron Beach Hotel Pattaya (තරු 3)",
    "Check in at 02.00 pm.": "ප.ව. 02.00 ට හෝටලයට ඇතුළත් වීම (Check-in).",
    
    # Day 2
    "Coral Island Tour by Speed Boat with Lunch": "දිවා ආහාරය සමඟ ස්පීඩ් බෝට්ටුවකින් කොරල් දූපත් චාරිකාව",
    "We will pick you up from your Pattaya hotel around 09:00 AM and transfer will begin. You will travel to Coral Island by speedboat.": "උදෑසන 09:00 ට පමණ පතායා හෝටලයෙන් ඔබව රැගෙන ගමන් ආරම්භ කරයි. ඔබ ස්පීඩ් බෝට්ටුවකින් කොරල් දූපත වෙත ගමන් කරනු ඇත.",
    "On the way, you can experience parasailing, jet skiing, and an under water walk ( These activities are not included in the package )": "අතරමගදී, ඔබට පැරසේලිං, ජෙට් ස්කීං සහ දිය යට ඇවිදීම අත්විඳිය හැකිය (මේවා පැකේජයට ඇතුළත් නොවේ)",
    "Lunch will be served at an Indian restaurant.": "ඉන්දියානු ආපනශාලාවකදී දිවා ආහාරය පිරිනමනු ලැබේ.",
    "(Lunch will be provided by the Coral Island boat company as a complimentary.)": "(දිවා ආහාරය කොරල් දූපත් බෝට්ටු සමාගම විසින් නොමිලේ සපයනු ලැබේ.)",
    "Pattaya Tiger Park": "පතායා ටයිගර් පාර්ක්",
    "At Pattaya Tiger Park, you can view and observe different types of tigers including giant Bengal tigers in a safe and well-managed environment.": "පතායා ටයිගර් පාර්ක් හිදී, ඔබට ආරක්ෂිත සහ මනාව කළමනාකරණය කළ පරිසරයක් තුළ යෝධ බෙංගාල කොටින් ඇතුළු විවිධ වර්ගයේ කොටින් නැරඹීමට සහ නිරීක්ෂණය කිරීමට හැකිය.",
    "Optional-You can choose to go in the cage (10-15 mins.) to feel, touch, hug and play with tigers.Also you can take pictures with tigers. ( These activities are not included in the package )": "විකල්ප - කොටින් දැනීමට, ස්පර්ශ කිරීමට, බදා ගැනීමට සහ සෙල්ලම් කිරීමට කූඩුවට යාමට (විනාඩි 10-15) ඔබට තෝරා ගත හැකිය. තවද ඔබට කොටින් සමඟ ඡායාරූප ගත හැකිය. (මේවා පැකේජයට ඇතුළත් නොවේ)",

    # Day 3
    "Morning": "උදෑසන",
    "After breakfast": "උදෑසන ආහාරයෙන් පසු",
    "check out from Pattaya hotel.": "පතායා හෝටලයෙන් පිටවීම (Check-out).",
    "You will be picked up from Pattaya Hotel &transferred to Bangkok": "පතායා හෝටලයෙන් ඔබව රැගෙන බැංකොක් වෙත ගමන් කරයි",
    "Sea life Bangkok Ocean World + Madame Tussauds Wax museum": "සී ලයිෆ් බැංකොක් ඕෂන් වර්ල්ඩ් + මැඩම් ටුසාඩ්ස් ඉටි රූප කෞතුකාගාරය",
    "Experience a fun-filled day in Bangkok with visits to SEA LIFE Bangkok Ocean World and Madame Tussauds Bangkok.": "සී ලයිෆ් බැංකොක් ඕෂන් වර්ල්ඩ් සහ මැඩම් ටුසාඩ්ස් බැංකොක් නැරඹීම සමඟ බැංකොක් නුවර විනෝදයෙන් පිරි දවසක් අත්විඳින්න.",
    "Discover fascinating marine life and walk through an exciting under water tunnel before enjoying interactive moments and photo opportunities with life like celebrity figures perfect for a memorable and entertaining city experience.": "සිත් ඇදගන්නාසුළු සාගර ජීවීන් සොයාගෙන ආකර්ෂණීය දිය යට උමඟක් හරහා ඇවිදින්න. ඉන්පසු ලොව ප්‍රසිද්ධ පුද්ගලයින්ගේ සැබෑවටම සමාන ඉටි රූප සමඟ අන්තර්ක්‍රියාකාරී අවස්ථා සහ ඡායාරූප ගැනීමේ අවස්ථා භුක්ති විඳින්න. මෙය අමතක නොවන නගර අත්දැකීමක් වනු ඇත.",
    "After the tour, you will be transferred to the Picnic 3* Hotel in Bangkok.": "චාරිකාවෙන් පසු, ඔබව බැංකොක් හි පික්නික් හෝටලය (තරු 3) වෙත ගෙන යනු ඇත.",
    "Check in at 02.00pm to Picnic HotelBangkok3*": "ප.ව. 02.00 ට පික්නික් හෝටලයට ඇතුළත් වීම (Check-in)",
    "Chao Phraya Cruise Dinner": "චාඕ ෆ්‍රායා කෲස් රාත්‍රී ආහාරය",
    "Get ready to be picked up at 05:00 PM for a magical evening on the Chao Phraya Dinner Cruise! Experience serene river cruise encompassing rich Thai royal history.": "චාඕ ෆ්‍රායා රාත්‍රී ආහාර කෲස් එකේ අපූරු සන්ධ්‍යාවක් සඳහා ප.ව. 05:00 ට සූදානම් වන්න! පොහොසත් තායි රාජකීය ඉතිහාසය වටා ගෙතුණු සන්සුන් ගංගා චාරිකාවක් අත්විඳින්න.",
    "Splendid illumination of Bangkok landmarks under neon lights.": "නියොන් ආලෝකය යටතේ බැංකොක් හි සන්ධිස්ථානවල අලංකාර ආලෝකකරණය.",
    "Delicious & tasty buffet with international delicacies": "ජාත්‍යන්තර ප්‍රණීත ආහාර සහිත රසවත් බුෆේ",

    # Day 4
    "After enjoying your breakfast, get ready for a 09:00AM pickup from the hotel for a fun-filled day at Dream World & Snow Town!": "උදෑසන ආහාරය භුක්ති විඳීමෙන් පසු, ඩ්‍රීම් වර්ල්ඩ් සහ ස්නෝ ටවුන් හි විනෝදයෙන් පිරි දවසක් සඳහා උදෑසන 09:00 ට හෝටලයෙන් පිටත් වීමට සූදානම් වන්න!",
    "Dream World & Snow Town with Lunch": "දිවා ආහාරය සමඟ ඩ්‍රීම් වර්ල්ඩ් සහ ස්නෝ ටවුන්",
    "Dream World & Snow Town has been a popular amusement park in Thailand for locals and tourists alike for many years.": "ඩ්‍රීම් වර්ල්ඩ් සහ ස්නෝ ටවුන් වසර ගණනාවක් පුරා ප්‍රදේශවාසීන් සහ සංචාරකයින් අතර තායිලන්තයේ ජනප්‍රිය විනෝද උද්‍යානයක් විය.",
    "Whether you are a fan of adventure activities or thrill rides, Dream World & Snow Town will be a definite hit no matter your age!": "ඔබ ත්‍රාසජනක ක්‍රියාකාරකම් වලට හෝ සවාරි වලට කැමති අයෙකු වුවද, ඔබේ වයස කුමක් වුවත් ඩ්‍රීම් වර්ල්ඩ් සහ ස්නෝ ටවුන් ඔබට අනිවාර්යයෙන්ම ගැලපෙනු ඇත!",
    "Around 04:00 PM , we will depart from Dream World.": "ප.ව. 04:00 ට පමණ අපි ඩ්‍රීම් වර්ල්ඩ් වෙතින් පිටත් වෙමු.",

    # Day 5
    "You’re free to relaxing or shopping to your satisfaction .": "ඔබට විවේක ගැනීමට හෝ ඔබේ සිතැඟි පරිදි සාප්පු සවාරි යාමට නිදහස ඇත.",
    "You’ll have free time to explore popular shopping locations like Platinum Mall, Indra Market, Big C, Palladium Mall, Central World, and more. Don’t worry we’ll walk you to all the best spots!": "Platinum Mall, Indra Market, Big C, Palladium Mall, Central World වැනි ජනප්‍රිය සාප්පු සවාරි ස්ථාන ගවේෂණය කිරීමට ඔබට නිදහස් කාලය ලැබෙනු ඇත. බිය නොවන්න, අපි ඔබව හොඳම ස්ථාන වලට මඟ පෙන්වන්නෙමු!",
    "Your Bangkok hotel is within walking distance of shopping malls.": "ඔබේ බැංකොක් හෝටලය සාප්පු සංකීර්ණ වලට ඇවිද යා හැකි දුරකින් පිහිටා ඇත.",
    
    # Day 6
    "Hotel check out 12.00PM": "දහවල් 12.00 ට හෝටලයෙන් පිටවීම (Check-out)",
    "You can leave your luggage at the hotel lobby until the airport pick-up time.": "ගුවන් තොටුපළ වෙත රැගෙන යන වේලාව දක්වා ඔබගේ ගමන් මලු හෝටලයේ ලොබියේ තබා යා හැක.",
    "04:00 PM: Pickup from your Bangkok hotel and transfer to DMK International Airport": "ප.ව. 04:00: ඔබගේ බැංකොක් හෝටලයෙන් පිටත් වී DMK ජාත්‍යන්තර ගුවන් තොටුපළ වෙත ගමන් කිරීම.",
    "Departure-Bangkok to Colomb": "පිටත් වීම - බැංකොක් සිට කොළඹ දක්වා",

    # Other strings that may appear in multiple places
    "Sightseeing": "දර්ශන නැරඹීම",
    "Tours": "චාරිකා",
    "Overnight Stay at Hotel": "රාත්‍රිය හෝටලයේ ගත කිරීම",
    "Breakfast at Hotel": "හෝටලයෙන් උදෑසන ආහාරය",
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

def rt(text, old, new):
    if text:
        return text.replace(old, new)
    return text

# Ensure we process other text blocks
texts = state.get('texts', {})
texts['durationBadge'] = 'රාත්‍රී 5ක් සහ දින 6ක්'
texts['dateBadge'] = rt(texts.get('dateBadge',''), '17 - 22 October 2026', '2026 ඔක්තෝබර් 17 - 22')

dp = texts.get('departureProcedure', '')
dp = rt(dp, 'Sun Leisure World’s representative will meet you at Colombo Bandaranayake International', 'සන් ලෙෂර් වර්ල්ඩ් ආයතනයේ නියෝජිතයෙකු ඔබව කොළඹ බණ්ඩාරනායක ජාත්‍යන්තර')
dp = rt(dp, 'Airport. You will get a briefing of the departure procedure', 'ගුවන් තොටුපළේදී හමුවනු ඇත. පිටවීමේ ක්‍රියාවලිය පිළිබඳව ඔබට දැනුවත් කිරීමක් ලැබෙන අතර')
dp = rt(dp, 'our representative will guide you in the process.', 'අපගේ නියෝජිතයා ඔබට එම ක්‍රියාවලිය සඳහා මඟ පෙන්වනු ඇත.')
texts['departureProcedure'] = dp

inc = texts.get('inclusions', '')
inc = rt(inc, 'Pattaya Tiger Park', 'පතායා ටයිගර් පාර්ක්')
inc = rt(inc, '(walk around ticket)', '(ඇවිදීමේ ටිකට් පත)')
inc = rt(inc, 'Pattaya Big Buddha Temple Tour', 'පතායා බිග් බුද්ධා විහාරස්ථාන චාරිකාව')
inc = rt(inc, 'Pattaya Dolphinarium', 'පතායා ඩොල්ෆිනාරියම්')
inc = rt(inc, 'Coral Island Tour by Speed Boat', 'ස්පීඩ් බෝට්ටුවකින් කොරල් දූපත් චාරිකාව')
inc = rt(inc, 'with Lunch', 'දිවා ආහාරය සමඟ')
inc = rt(inc, 'Sea life Bangkok Ocean World + Madame Tussauds Wax Museum', 'සී ලයිෆ් බැංකොක් ඕෂන් වර්ල්ඩ් + මැඩම් ටුසාඩ්ස් ඉටි රූප කෞතුකාගාරය')
inc = rt(inc, 'Chao Phraya Cruise Dinner', 'චාඕ ෆ්‍රායා කෲස් රාත්‍රී ආහාරය')
inc = rt(inc, 'Dream World', 'ඩ්‍රීම් වර්ල්ඩ්')
inc = rt(inc, 'SnowTown with Lunch', 'ස්නෝ ටවුන් දිවා ආහාරය සමඟ')
inc = rt(inc, 'Allabove-mentioned tour admissionfees.', 'ඉහත සඳහන් කළ සියලුම චාරිකා ප්‍රවේශ ගාස්තු.')
inc = rt(inc, 'All airport &', 'සියලුම ගුවන් තොටුපළ සහ')
inc = rt(inc, 'Tour T', 'චාරිකා ප්‍ර')
inc = rt(inc, 'ransfers by luxury air-conditioned bus.', 'වාහන පහසුකම් සුඛෝපභෝගී වායුසමනය කළ බස් රථ මගින්.')
inc = rt(inc, '05Nights at 3* Hotel Accommodation', 'තරු 3 (3*) හෝටල්වල රාත්‍රී 05 ක නවාතැන්.')
inc = rt(inc, 'Thailand Professional Tour Guide.', 'තායිලන්ත වෘත්තීය චාරිකා මාර්ගෝපදේශක.')
inc = rt(inc, 'Tour manager from', 'සන් ලෙෂර් වර්ල්ඩ් (පුද්.) සමාගමෙන්')
inc = rt(inc, 'Sun Leisure World Pvt.Ltd.', 'චාරිකා කළමනාකරුවෙකු.')
inc = rt(inc, 'Air Ticket(Air Asia)', 'ගුවන් ටිකට් පත (Air Asia)')
inc = rt(inc, 'Breakfast 05 / Lunch 05 / Dinner 1', 'උදෑසන ආහාර 5 / දිවා ආහාර 5 / රාත්‍රී ආහාර 1')
texts['inclusions'] = inc

exc = texts.get('exclusions', '')
exc = rt(exc, 'Everything which is not mentioned inthe above program', 'ඉහත වැඩසටහනේ සඳහන් නොවන සියලුම දේ')
texts['exclusions'] = exc

fn = texts.get('flightNote', '')
fn = rt(fn, 'INCLUDED - MEALS + 20KG+07KG (both ways)', 'ඇතුළත් කර ඇත - ආහාර + 20KG+07KG (ගමන් වාර දෙකටම)')
texts['flightNote'] = fn


for day in state.get('days', []):
    desc = day.get('description', '')
    day['description'] = translate_html(desc)
    
    h = day.get('header', '')
    h = rt(h, 'Day 01', 'දිනය 01')
    h = rt(h, 'Day 02', 'දිනය 02')
    h = rt(h, 'Day 03', 'දිනය 03')
    h = rt(h, 'Day 04', 'දිනය 04')
    h = rt(h, 'Day 05', 'දිනය 05')
    h = rt(h, 'Day 06', 'දිනය 06')
    h = rt(h, 'Pattaya to Bangkok', 'පතායා සිට බැංකොක් දක්වා')
    h = rt(h, 'Pattaya', 'පතායා')
    h = rt(h, 'Bangkok', 'බැංකොක්')
    day['header'] = h

    dt = day.get('date', '')
    dt = rt(dt, 'Date', 'දිනය')
    day['date'] = dt

    mp = day.get('mealPlan', '')
    mp = rt(mp, 'Breakfast', 'උදෑසන ආහාරය')
    mp = rt(mp, 'Lunch', 'දිවා ආහාරය')
    mp = rt(mp, 'Dinner', 'රාත්‍රී ආහාරය')
    day['mealPlan'] = mp

# Prices & Reviews
for p in state.get('prices', []):
    c = p.get('category', '')
    c = rt(c, 'Adult Price', 'වැඩිහිටි ගාස්තුව')
    c = rt(c, 'Child Sharing Bed Price', 'ඇඳක් බෙදාගන්නා ළමා ගාස්තුව')
    p['category'] = c

for r in state.get('reviews', []):
    t = r.get('text', '')
    t = rt(t, 'Thank You So Mach Sun Leisure World Sri Lanka ..', 'බොහොම ස්තූතියි Sun Leisure World Sri Lanka ..')
    t = rt(t, 'The trip was well organised and the coordination from you and Thailand Guide Thank you for all your support Chathura', 'චාරිකාව ඉතා හොඳින් සංවිධානය කර තිබූ අතර ඔබගේ සහ තායිලන්ත මාර්ගෝපදේශකයාගේ සම්බන්ධීකරණය ඉතා විශිෂ්ටයි. ඔබගේ සහයෝගයට ස්තූතියි චතුර.')
    t = rt(t, 'I would like to extend my sincere appreciation to Sun Leisure World for their impeccable service and commitment to excellence. Their team demonstrates a level of professionalism and attention to detail that truly sets a benchmark in the industry. The entire experience was flawlessly managed, making our journey both memorable and stress-free. I highly recommend their services to any discerning traveler seeking a premium experience', 'ඔවුන්ගේ දෝෂ රහිත සේවාව සහ විශිෂ්ටත්වය වෙනුවෙන් Sun Leisure World වෙත මාගේ අවංක කෘතඥතාවය පළ කිරීමට කැමැත්තෙමි. ඔවුන්ගේ කණ්ඩායම කර්මාන්තයේ සැබෑ මිණුම් ලකුණක් තබන වෘත්තීයභාවයක් සහ සවිස්තරාත්මක අවධානයක් පෙන්නුම් කරයි. මුළු අත්දැකීමම දෝෂ රහිතව කළමනාකරණය කර තිබූ අතර අපගේ ගමන අමතක නොවන සහ ආතතියෙන් තොර එකක් බවට පත් කළේය. වාරික අත්දැකීමක් අපේක්ෂා කරන ඕනෑම සංචාරකයෙකුට මම ඔවුන්ගේ සේවාවන් ඉතා ඉහළින් නිර්දේශ කරමි.')
    t = rt(t, 'We joined a group tour on April (which songkran festival days) had an amazing 6 days in Pathaya & Bangkok. Well planned, experienced guide, safe and comfortable transportation. hotels are located near iconic location. Highly recommended for familys, couples and groups for your next travel destination. Hopefully, we willing to join another tour with sun leisure world. Also mr. Chathura gave us a fantastic guidance and a headache free friendly service', 'අපි අප්‍රේල් මාසයේ (සොන්ක්‍රන් උත්සව දිනවල) කණ්ඩායම් චාරිකාවකට සහභාගී වූ අතර පතායා සහ බැංකොක් හි පුදුමාකාර දින 6ක් ගත කළෙමු. හොඳින් සැලසුම් කර තිබුණි, පළපුරුදු මාර්ගෝපදේශකයෙක්, ආරක්ෂිත සහ සුවපහසු ප්‍රවාහනය. හෝටල් ප්‍රධාන ස්ථාන අසල පිහිටා තිබුණි. පවුල්, ජෝඩු සහ කණ්ඩායම් සඳහා ඊළඟ සංචාරක ගමනාන්තය ලෙස බෙහෙවින් නිර්දේශ කරනු ලැබේ. අපි තවත් සංචාරයක් සඳහා Sun Leisure World සමඟ එකතු වීමට බලාපොරොත්තු වෙමු. එසේම චතුර මහතා අපට අපූරු මගපෙන්වීමක් සහ කිසිදු කරදරයකින් තොර මිත්‍රශීලී සේවාවක් ලබා දුන්නේය.')
    r['text'] = t

state['tourName'] = 'බැංකොක් – පතායා කණ්ඩායම් චාරිකාව'

with open('Group tour Sinhala.html', 'r', encoding='utf-8') as f:
    html = f.read()

start = html.find('// /* STATE_START */')
end = html.find('// /* STATE_END */')

# USE ensure_ascii=False to save unicode properly in HTML script tag
state_json_str = json.dumps(state, indent=4, ensure_ascii=False)
original_state_block = html[start:end]
new_state_block = '// /* STATE_START */\n                const state = reactive(' + state_json_str + ');\n                '
html = html[:start] + new_state_block + html[end:]

with open('Group tour Sinhala.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Done injecting state exactly using beautifulsoup substring replace with unescaped unicode.')
