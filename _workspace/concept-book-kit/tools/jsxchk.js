const B = require('/home/claude/pbtest/node_modules/@babel/standalone');
for (const f of process.argv.slice(2)) { try { B.transform(require('fs').readFileSync(f, 'utf8'), { presets: ['react'] }); console.log('ok', f); } catch (e) { console.log('ERR', f, e.message.slice(0, 300)); } }
