(function () {
  const btn = document.getElementById('avatarBtn');
  const menu = document.getElementById('profileMenu');
  if (!btn || !menu) return;

  function closeMenu() {
    menu.classList.remove('open');
    btn.setAttribute('aria-expanded', 'false');
  }
  function toggleMenu() {
    const open = menu.classList.toggle('open');
    btn.setAttribute('aria-expanded', String(open));
  }

  btn.addEventListener('click', (e) => {
    e.stopPropagation();
    toggleMenu();
  });

  document.addEventListener('click', (e) => {
    if (!menu.contains(e.target) && e.target !== btn) closeMenu();
  });

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') closeMenu();
  });
})();
