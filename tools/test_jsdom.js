const fs = require('fs');
const jsdom = require("jsdom");
const { JSDOM } = jsdom;
const virtualConsole = new jsdom.VirtualConsole();

virtualConsole.on("error", (err) => {
  console.error("Browser Error:", err);
});
virtualConsole.on("log", (log) => {
  console.log("Browser Log:", log);
});
virtualConsole.on("warn", (warn) => {
  console.warn("Browser Warn:", warn);
});
virtualConsole.on("jsdomError", (e) => {
  console.error("JSDOM Error:", e.stack, e.detail);
});

const html = fs.readFileSync('group_tour_builder.html', 'utf8');

const dom = new JSDOM(html, {
  runScripts: "dangerously",
  resources: "usable",
  virtualConsole
});

setTimeout(() => {
    console.log("App HTML inside #app length:", dom.window.document.getElementById('app').innerHTML.length);
    console.log("Done waiting");
    process.exit(0);
}, 3000);
