import os

def refactor_html(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    replacements = [
        # 1. tourName
        (
            '<h1 class="text-4xl font-extrabold text-white leading-tight drop-shadow-md mb-2" contenteditable="true" @blur="state.tourName = $event.target.innerText" @focus="startDragSpacer(\'page1\', $event)">\n                                {{ state.tourName }}\n                            </h1>',
            '<h1 class="text-4xl font-extrabold text-white leading-tight drop-shadow-md mb-2" contenteditable="true" @blur="state.tourName = $event.target.innerText" @focus="startDragSpacer(\'page1\', $event)" v-html="state.tourName"></h1>'
        ),
        (
            '<h1 class="text-3xl font-bold text-sun-green mb-2 font-serif uppercase w-full" contenteditable="true" @blur="state.tourName = $event.target.innerText">\n                            {{ state.tourName }}\n                        </h1>',
            '<h1 class="text-3xl font-bold text-sun-green mb-2 font-serif uppercase w-full" contenteditable="true" @blur="state.tourName = $event.target.innerText" v-html="state.tourName"></h1>'
        ),
        # 2. durationBadge
        (
            '<span class="bg-sun-blue text-white px-3 py-1 rounded-full text-sm font-bold shadow-sm inline-block" contenteditable="true">5 Nights 6 Days</span>',
            '<span class="bg-sun-blue text-white px-3 py-1 rounded-full text-sm font-bold shadow-sm inline-block" contenteditable="true" @blur="state.texts.durationBadge = $event.target.innerHTML" v-html="state.texts.durationBadge"></span>'
        ),
        # 3. dateBadge
        (
            '<h2 class="text-xl text-sun-orange font-semibold" contenteditable="true">23 - 28 August 2026</h2>',
            '<h2 class="text-xl text-sun-orange font-semibold" contenteditable="true" @blur="state.texts.dateBadge = $event.target.innerHTML" v-html="state.texts.dateBadge"></h2>'
        ),
        # 4. departureProcedure
        (
            '<div class="text-sm" contenteditable="true">\n                            <ul>\n                                <li>Sun Leisure World\'s representative will meet you at Colombo Bandaranayake International Airport.</li>\n                                <li>You will get a briefing of the departure procedure & our representative will guide you in the process.</li>\n                            </ul>\n                        </div>',
            '<div class="text-sm" contenteditable="true" @blur="state.texts.departureProcedure = $event.target.innerHTML" v-html="state.texts.departureProcedure"></div>'
        ),
        # 5. day.header
        (
            '<span class="day-header" :class="idx === state.days.length - 1 ? \'bg-sun-orange\' : \'\'" contenteditable="true">Day {{ String(idx+1).padStart(2, \'0\') }} – City Name</span>',
            '<span class="day-header" :class="idx === state.days.length - 1 ? \'bg-sun-orange\' : \'\'" contenteditable="true" @blur="day.header = $event.target.innerHTML" v-html="day.header"></span>'
        ),
        # 6. day.date
        (
            '<span class="ml-3 text-sm font-semibold text-gray-500 bg-gray-100 px-2 py-1 rounded" contenteditable="true">Date (e.g. 23/08)</span>',
            '<span class="ml-3 text-sm font-semibold text-gray-500 bg-gray-100 px-2 py-1 rounded" contenteditable="true" @blur="day.date = $event.target.innerHTML" v-html="day.date"></span>'
        ),
        # 7. day.mealPlan
        (
            '<span contenteditable="true">Breakfast, Lunch</span>',
            '<span contenteditable="true" @blur="day.mealPlan = $event.target.innerHTML" v-html="day.mealPlan"></span>'
        ),
        # 8. day.description
        (
            '<div contenteditable="true" class="space-y-2 mt-2 min-h-[40px]">\n                                    <p>Description of the day\'s activities goes here. You can type freely.</p>\n                                </div>',
            '<div contenteditable="true" class="space-y-2 mt-2 min-h-[40px]" @blur="day.description = $event.target.innerHTML" v-html="day.description"></div>'
        ),
        # 9. inclusions
        (
            '<div contenteditable="true" class="text-sm text-gray-700 min-h-[100px]">\n                                <ul class="list-disc pl-5 space-y-1.5">\n                                    <li>All mentioned tours & admission fees</li>\n                                    <li>Coral Island Tour by Speedboat</li>\n                                    <li>05 Nights at 3* hotel in Pattaya & BKK</li>\n                                </ul>\n                            </div>',
            '<div contenteditable="true" class="text-sm text-gray-700 min-h-[100px]" @blur="state.texts.inclusions = $event.target.innerHTML" v-html="state.texts.inclusions"></div>'
        ),
        # 10. exclusions
        (
            '<div contenteditable="true" class="text-sm text-gray-700 min-h-[100px]">\n                                <ul class="list-disc pl-5 space-y-1.5">\n                                    <li>Early check-in or late check-out</li>\n                                    <li>Personal expenses</li>\n                                    <li>Tips for guide & driver</li>\n                                </ul>\n                            </div>',
            '<div contenteditable="true" class="text-sm text-gray-700 min-h-[100px]" @blur="state.texts.exclusions = $event.target.innerHTML" v-html="state.texts.exclusions"></div>'
        ),
        # 11. flightDeparture
        (
            '<span contenteditable="true">Colombo to Bangkok - FD 141 – CMB-DMK - 23:15-04:20(+1)</span>',
            '<span contenteditable="true" @blur="state.texts.flightDeparture = $event.target.innerHTML" v-html="state.texts.flightDeparture"></span>'
        ),
        # 12. flightReturn
        (
            '<span contenteditable="true">Bangkok to Colombo - FD 140 – DMK-CMB - 20:25-22:15</span>',
            '<span contenteditable="true" @blur="state.texts.flightReturn = $event.target.innerHTML" v-html="state.texts.flightReturn"></span>'
        ),
        # 13. flightNote
        (
            '<p class="text-gray-500 mt-2 italic border-t pt-2" contenteditable="true">Note: Meals + 20KG Baggage + 7KG Hand Luggage included.</p>',
            '<p class="text-gray-500 mt-2 italic border-t pt-2" contenteditable="true" @blur="state.texts.flightNote = $event.target.innerHTML" v-html="state.texts.flightNote"></p>'
        ),
        # 14. review.name
        (
            '<h5 class="font-bold text-sm text-gray-800" contenteditable="true">Traveler Name</h5>',
            '<h5 class="font-bold text-sm text-gray-800" contenteditable="true" @blur="review.name = $event.target.innerHTML" v-html="review.name"></h5>'
        ),
        # 15. review.text
        (
            '<p class="text-xs text-gray-600 italic leading-relaxed" contenteditable="true">"Type the review here..."</p>',
            '<p class="text-xs text-gray-600 italic leading-relaxed" contenteditable="true" @blur="review.text = $event.target.innerHTML" v-html="review.text"></p>'
        )
    ]

    for old, new in replacements:
        if old not in html:
            # Fallbacks for encoding differences or slight whitespace issues
            print(f"Warning: Could not find exact match for {old[:40]}...")
        html = html.replace(old, new)
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
        
    print("HTML refactor completed!")

if __name__ == '__main__':
    refactor_html('group_tour_builder.html')
