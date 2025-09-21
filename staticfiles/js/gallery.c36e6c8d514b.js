(function(){
  const btn = document.getElementById('galleryModeToggle');
  if(!btn) return;

  const KEY = 'vixi-gallery-theme';
  function apply(mode){
    const dark = mode === 'dark';
    document.body.classList.toggle('dark', dark);
    btn.textContent = dark ? '☀' : '☾';
    btn.setAttribute('aria-pressed', String(dark));
  }

  apply(localStorage.getItem(KEY) || 'light');

  btn.addEventListener('click', ()=>{
    const dark = !document.body.classList.contains('dark');
    apply(dark ? 'dark' : 'light');
    localStorage.setItem(KEY, dark ? 'dark' : 'light');
  });
})();
