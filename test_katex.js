const fs = require('fs');
const path = require('path');

const html = fs.readFileSync(path.join('C:', 'Users', 'WALTON', 'Downloads', 'dari-backup', 'dari', 'question_bank_viewer.html'), 'utf8');

const match = html.match(/const APP_DATA = (\{[\s\S]+?\});\r?\n/);
const data = JSON.parse(match[1]);

// Check what katex assets exist
let katexJs = null;
const katexJsPath = path.join('C:', 'Users', 'WALTON', 'Downloads', 'dari-backup', 'dari', 'katex_dist', 'katex.min.js');
if (fs.existsSync(katexJsPath)) {
  const content = fs.readFileSync(katexJsPath, 'utf8');
  // Evaluate in sandbox
  const vm = require('vm');
  const ctx = { window: {}, document: {}, navigator: {} };
  vm.createContext(ctx);
  vm.runInContext(content, ctx);
  katex = ctx.katex || ctx.window.katex;
}

console.log('KaTeX loaded?', !!katex);

const re = /\$\$([\s\S]+?)\$\$|\$([\s\S]+?)\$/g;
let errorCount = 0;
let errors = [];

data.questions.forEach((q) => {
  const texts = [
    { name: 'q', text: q.q },
    { name: 'a', text: q.a },
    { name: 'e', text: q.e },
    ...(q.o || []).map((opt, i) => ({ name: `o${i}`, text: opt }))
  ].filter(item => Boolean(item.text));

  texts.forEach(item => {
    const txt = item.text;
    let m;
    const regex = new RegExp(re);
    while ((m = regex.exec(txt)) !== null) {
      const code = m[1] !== undefined ? m[1] : m[2];
      if (katex) {
        try {
          katex.renderToString(code, { throwOnError: true, displayMode: m[1] !== undefined });
        } catch (err) {
          errorCount++;
          if (errors.length < 30) {
            errors.push({ qNum: q.n, field: item.name, code, msg: err.message });
          }
        }
      }
    }
  });
});

console.log('Total KaTeX syntax errors in data:', errorCount);
console.log('Sample errors:', JSON.stringify(errors, null, 2));
