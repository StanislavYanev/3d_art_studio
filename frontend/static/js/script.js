
const toggleBtn = document.getElementById('menu-toggle');
const navMenu = document.getElementById('menu');
const overlay = document.getElementById('menu-overlay');

toggleBtn.addEventListener('click', () => {
  toggleBtn.classList.toggle('open');
  navMenu.classList.toggle('show');
  overlay.classList.toggle('active');
});

document.querySelectorAll('#menu a').forEach(link => {
  link.addEventListener('click', () => {
    toggleBtn.classList.remove('open');
    navMenu.classList.remove('show');
    overlay.classList.remove('active');
  });
});

overlay.addEventListener('click', () => {
  toggleBtn.classList.remove('open');
  navMenu.classList.remove('show');
  overlay.classList.remove('active');
});
