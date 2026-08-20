const fs = require('fs');
const path = require('path');

const html = fs.readFileSync(path.join('C:', 'Users', 'WALTON', 'Downloads', 'dari-backup', 'dari', 'question_bank_viewer.html'), 'utf8');

const match = html.match(/const APP_DATA = (\{[\s\S]+?\});\r?\n/);
if (!match) {
  console.error("APP_DATA not found in HTML!");
  process.exit(1);
}

const data = JSON.parse(match[1]);
console.log("Total questions:", data.questions.length);
console.log("Stats:", data.stats);

// Check KaTeX
const katexJsPath = path.join('C:', 'Users', 'WALTON', 'Downloads', 'dari-backup', 'dari', 'katex_dist', 'katex.min.js');
let katex = null;
if (fs.existsSync(katexJsPath)) {
  const content = fs.readFileSync(katexJsPath, 'utf8');
  const vm = require('vm');
  const ctx = { window: {}, document: {}, navigator: {} };
  vm.createContext(ctx);
  vm.runInContext(content, ctx);
  katex = ctx.katex || ctx.window.katex;
}

const mathRegex = /\$\$([\s\S]+?)\$\$|\\\[([\s\S]+?)\\\]|\$([\s\S]+?)\$|\\\(([\s\S]+?)\\\)/g;
let errorCount = 0;
let errors = [];

data.questions.forEach((q) => {
  const texts = [q.q, q.a, q.e, ...(q.o || [])].filter(Boolean);
  texts.forEach(txt => {
    let m;
    const re = new RegExp(mathRegex);
    while ((m = re.exec(txt)) !== null) {
      const code = m[1] || m[2] || m[3] || m[4];
      if (katex) {
        try {
          katex.renderToString(code.trim(), { throwOnError: true, displayMode: !!(m[1] || m[2]), strict: false });
        } catch (err) {
          errorCount++;
          if (errors.length < 10) {
            errors.push({ qNum: q.n, code, msg: err.message });
          }
        }
      }
    }
  });
});

console.log("KaTeX parsing errors:", errorCount);
if (errors.length > 0) {
  console.log("Errors:", errors);
}

// Check sample defective questions
const checkNums = [92, 126, 192, 546, 548, 582, 583, 590, 591, 618, 678, 720];
checkNums.forEach(n => {
  const q = data.questions[n - 1];
  console.log(`\n=== Verified Q${n} ===`);
  console.log(`Question: ${q.q.substring(0, 60)}...`);
  console.log(`Option count: ${q.o ? q.o.length : 0}, Solution Index: ${q.i}`);
  if (q.o && q.i >= 0 && q.o[q.i]) {
    console.log(`Selected Ans Option (${['ক','খ','গ','ঘ','ঙ'][q.i]}): ${q.o[q.i]}`);
  }
  console.log(`Answer Text: ${q.a}`);
  console.log(`Explanation snippet: ${q.e ? q.e.substring(0, 80) : 'none'}...`);
  console.log(`Sources: ${JSON.stringify(q.s)}`);
});
