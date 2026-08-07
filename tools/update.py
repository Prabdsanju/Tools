import sys
from pathlib import Path

content = Path('group_tour_builder.html').read_text(encoding='utf-8')

# 1. Add pageBreakBefore toggle
target1 = """<div v-for="(day, idx) in state.days" :key="day.id" class="timeline-line pb-6 hover-group relative" :style="idx === state.days.length - 1 ? 'border-left-color: transparent;' : ''">
                            
                            <!-- Day Delete Button -->
                            <button class="delete-btn -right-10" @click="state.days.splice(idx, 1)" title="Remove Day"><i class="fas fa-trash text-xs"></i></button>"""

replacement1 = """<div v-for="(day, idx) in state.days" :key="day.id" class="timeline-line pb-6 hover-group relative" :style="idx === state.days.length - 1 ? 'border-left-color: transparent;' : ''">
                            <div v-if="day.pageBreakBefore" class="html2pdf__page-break"></div>
                            <!-- Day Page Break Toggle -->
                            <button class="no-print absolute -top-8 right-16 text-xs bg-gray-200 hover:bg-gray-300 rounded px-2 py-1 text-gray-700 opacity-0 group-hover:opacity-100 transition" @click="day.pageBreakBefore = !day.pageBreakBefore" title="Toggle Page Break Before">
                                <i class="fas fa-cut"></i> {{ day.pageBreakBefore ? 'Remove Page Break' : 'Add Page Break' }}
                            </button>
                            <!-- Day Delete Button -->
                            <button class="delete-btn -right-10" @click="state.days.splice(idx, 1)" title="Remove Day"><i class="fas fa-trash text-xs"></i></button>"""

if target1 not in content:
    print('Failed to find target1')
    sys.exit(1)
content = content.replace(target1, replacement1)

# 2. Add promptImageUrl method
target2 = """// --- UPLOAD LOGIC ---
                function triggerUpload(type, index1 = null, index2 = null) {"""

replacement2 = """// --- UPLOAD LOGIC ---
                function promptImageUrl(type, index1 = null, index2 = null) {
                    const url = window.prompt("Enter the Image URL:");
                    if (url && url.trim() !== '') {
                        if (type === 'dayImage') {
                            const day = state.days[index1];
                            if (day && day.images) day.images.push(url);
                        }
                    }
                }

                function triggerUpload(type, index1 = null, index2 = null) {"""

if target2 not in content:
    print('Failed to find target2')
    sys.exit(1)
content = content.replace(target2, replacement2)

# 3. Modify day images rendering block
target3 = """<div class="edit-overlay rounded" @click="triggerUpload('dayImage', idx, i)">Upload</div>"""

replacement3 = """<div class="edit-overlay rounded flex-col gap-2 !cursor-default" style="pointer-events: auto;">
                                                <button @click.stop="triggerUpload('dayImage', idx, i)" class="bg-blue-600 hover:bg-blue-700 px-2 py-1 rounded w-3/4">Upload</button>
                                                <button @click.stop="promptImageUrl('dayImage', idx, i)" class="bg-green-600 hover:bg-green-700 px-2 py-1 rounded w-3/4">From URL</button>
                                            </div>"""

if target3 not in content:
    print('Failed to find target3')
    sys.exit(1)
content = content.replace(target3, replacement3)

# 4. Modify state.days initialization
target4 = """days: [
                        { id: Date.now(), images: ['https://images.unsplash.com/photo-1540420773420-3366772f4999?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80'] },
                        { id: Date.now()+1, images: [] }
                    ],"""

replacement4 = """days: [
                        { id: Date.now(), images: ['https://images.unsplash.com/photo-1540420773420-3366772f4999?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80'], pageBreakBefore: false },
                        { id: Date.now()+1, images: [], pageBreakBefore: false }
                    ],"""

if target4 not in content:
    print('Failed to find target4')
    sys.exit(1)
content = content.replace(target4, replacement4)

# 5. addDay initialization
target5 = """function addDay() {
                    state.days.push({ id: Date.now(), images: [] });
                }"""

replacement5 = """function addDay() {
                    state.days.push({ id: Date.now(), images: [], pageBreakBefore: false });
                }"""

if target5 not in content:
    print('Failed to find target5')
    sys.exit(1)
content = content.replace(target5, replacement5)

# 6. export
target6 = """printDoc,
                    exportPDF
                }"""

replacement6 = """printDoc,
                    exportPDF,
                    promptImageUrl
                }"""

if target6 not in content:
    print('Failed to find target6')
    sys.exit(1)
content = content.replace(target6, replacement6)

Path('group_tour_builder.html').write_text(content, encoding='utf-8')
print('Success')
