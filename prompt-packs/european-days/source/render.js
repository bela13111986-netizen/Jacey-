const {chromium}=require('playwright');
(async()=>{
 const b=await chromium.launch();
 for (const lang of ['ru','en']){
  const p=await b.newPage();
  await p.goto('file://'+__dirname+'/'+lang+'.html',{waitUntil:'networkidle'});
  await p.evaluate(()=>document.fonts.ready);
  const over=await p.evaluate(()=>[...document.querySelectorAll('.page')].map((s,i)=>{
    const f=s.querySelector('.foot'); const limit=f?f.getBoundingClientRect().top-4:s.getBoundingClientRect().bottom;
    let mx=0; s.querySelectorAll('*').forEach(el=>{if(el.closest('.foot')||el.classList.contains('bleed')||el.classList.contains('cv-shade'))return; const r=el.getBoundingClientRect(); if(r.height>0) mx=Math.max(mx,r.bottom)});
    return mx>limit?[i+1,Math.round(mx-limit)]:null}).filter(Boolean));
  const fonts=await p.evaluate(()=>[...document.fonts].filter(f=>f.status=='loaded').map(f=>f.family+' '+f.style).slice(0,6));
  console.log(lang,'overflow pages:',JSON.stringify(over),'fonts:',fonts.join(','));
  await p.pdf({path:__dirname+'/'+lang+'.pdf',printBackground:true,preferCSSPageSize:true});
 }
 await b.close();})();
