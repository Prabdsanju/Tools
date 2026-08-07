const compiler = require('@vue/compiler-dom');
const fs = require('fs');
const code = fs.readFileSync('group_tour_builder.html', 'utf8');
const templateMatch = code.match(/<div id="app"[^>]*>([\s\S]*?)<\/div>\s*<!-- Floating Rich Text Toolbar -->/);
const template = templateMatch[1];
try {
  compiler.compile(template);
  console.log("Success");
} catch (e) {
  console.log('Error:', e.message);
  console.log('Line:', e.loc.start.line);
  console.log('Code context:');
  const lines = template.split('\n');
  console.log(lines[e.loc.start.line - 1]);
}
