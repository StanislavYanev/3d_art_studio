const toggle = document.getElementById("menu-toggle");
const mobileMenu = document.getElementById("mobile-menu");
toggle?.addEventListener("click", () => {
  mobileMenu.classList.toggle("hidden");
});

function scrollCarouselLeft(btn) {
  const carousel = btn.nextElementSibling;
  carousel.scrollBy({ left: -200, behavior: 'smooth' });
}

function scrollCarouselRight(btn) {
  const carousel = btn.previousElementSibling;
  carousel.scrollBy({ left: 200, behavior: 'smooth' });
}

function openLightbox(url) {
  const modal = document.getElementById("lightbox-modal");
  const img = document.getElementById("lightbox-img");
  img.src = url;
  modal.classList.remove("hidden");
}

function closeLightbox() {
  const modal = document.getElementById("lightbox-modal");
  const img = document.getElementById("lightbox-img");
  img.src = "";
  modal.classList.add("hidden");
}
