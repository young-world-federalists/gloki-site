// Render the share images and the comparison sheets.
// Run from anywhere: node shoot.js   (serves nothing itself; sheets need
// `python3 -m http.server 8765` running in /home/user/gloki-site)
const { chromium } = require('playwright');
const path = require('path');
const OUT = path.resolve(__dirname, '..');
(async () => {
  const b = await chromium.launch();
  const which = process.argv[2] || 'all';
  if (which === 'all' || which === 'og') {
    const p = await b.newPage({ viewport: { width: 1200, height: 630 }, deviceScaleFactor: 1 });
    for (const r of ['a', 'b', 'c']) {
      await p.goto('file://' + OUT + `/share/og-${r}.svg`);
      await p.screenshot({ path: OUT + `/share/og-${r}.png` });
    }
    await p.close();
  }
  if (which === 'all' || which === 'sheets') {
    const p = await b.newPage({ viewport: { width: 1600, height: 1000 }, deviceScaleFactor: 1.5 });
    for (const r of ['a', 'b', 'c']) {
      await p.goto(`http://localhost:8765/docs/brand/2026-10-26/sheets/sheet.html?route=${r}`);
      await p.waitForFunction(() => window.sheetReady === true, null, { timeout: 15000 });
      await p.waitForTimeout(2600); // let the hero animation in the iframes finish
      await p.screenshot({ path: OUT + `/sheets/sheet-${r}.png`, fullPage: true });
    }
    await p.close();
  }
  await b.close();
})();
