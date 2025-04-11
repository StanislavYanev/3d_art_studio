
const toggle = document.getElementById("menu-toggle");
const mobileMenu = document.getElementById("mobile-menu");
toggle?.addEventListener("click", () => {
  mobileMenu.classList.toggle("hidden");
});

const html = document.documentElement;
const sunIcon = document.getElementById("icon-sun");
const moonIcon = document.getElementById("icon-moon");
const themeToggle = document.getElementById("theme-toggle");

function updateThemeIcons() {
  const isDark = html.classList.contains("dark");
  sunIcon.classList.toggle("hidden", !isDark);
  moonIcon.classList.toggle("hidden", isDark);
}

if (
  localStorage.theme === "dark" ||
  (!localStorage.theme &&
    window.matchMedia("(prefers-color-scheme: dark)").matches)
) {
  html.classList.add("dark");
}

updateThemeIcons();

themeToggle?.addEventListener("click", () => {
  html.classList.toggle("dark");
  localStorage.theme = html.classList.contains("dark") ? "dark" : "light";
  updateThemeIcons();
});

document.getElementById("open-cart")?.addEventListener("click", () => {
  document.getElementById("cart-modal")?.classList.remove("hidden");
  document.getElementById("cart-modal")?.classList.add("flex");
  fetch('{% url "cart:cart_detail" %}', {
    headers: {
      "X-Requested-With": "XMLHttpRequest",
    },
  })
    .then((res) => res.text())
    .then((html) => {
      document.getElementById("cart-content").innerHTML = html;
    });
});

function closeCartModal() {
  const modal = document.getElementById("cart-modal");
  modal?.classList.remove("flex");
  modal?.classList.add("hidden");
}
function removeFromCart(productId) {
  fetch(`/cart/remove/${productId}/`, {
    method: 'POST',
    headers: {
      'X-CSRFToken': getCSRFToken(),
      'X-Requested-With': 'XMLHttpRequest'
    }
  })
  .then(res => {
    if (res.ok) {
      // Обнови съдържанието на модала
      return fetch('{% url "cart:cart_detail" %}', {
        headers: { 'X-Requested-With': 'XMLHttpRequest' }
      });
    }
  })
  .then(res => res.text())
  .then(html => {
    document.getElementById('cart-content').innerHTML = html;
  });
}

function getCSRFToken() {
  return document.querySelector('[name=csrfmiddlewaretoken]')?.value;
}  
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

function increaseQty(id) {
  const input = document.getElementById(id);
  input.value = parseInt(input.value || 1) + 1;
}

function decreaseQty(id) {
  const input = document.getElementById(id);
  if (parseInt(input.value) > 1) {
    input.value = parseInt(input.value) - 1;
  }
}

function openModal(id) {
  const modal = document.getElementById(`modal-${id}`);
  const content = document.getElementById(`modal-content-${id}`);
  modal.classList.remove("hidden");
  modal.classList.add("flex");
  setTimeout(() => {
    content.classList.remove("scale-95", "opacity-0");
    content.classList.add("scale-100", "opacity-100");
  }, 10);
  document.body.classList.add("overflow-hidden");
  document.addEventListener("keydown", function escHandler(e) {
    if (e.key === "Escape") {
      closeModal(id);
      document.removeEventListener("keydown", escHandler);
    }
  });
}

function closeModal(id) {
  const modal = document.getElementById(`modal-${id}`);
  const content = document.getElementById(`modal-content-${id}`);
  content.classList.remove("scale-100", "opacity-100");
  content.classList.add("scale-95", "opacity-0");
  setTimeout(() => {
    modal.classList.remove("flex");
    modal.classList.add("hidden");
    document.body.classList.remove("overflow-hidden");
  }, 300);
}

function showToast(message) {
  const toast = document.getElementById("toast");
  const messageBox = document.getElementById("toast-message");
  messageBox.innerText = message;
  toast.classList.remove("hidden", "opacity-0", "scale-95");
  toast.classList.add("opacity-100", "scale-100");
  setTimeout(() => hideToast(), 5000);
}

function hideToast() {
  const toast = document.getElementById("toast");
  toast.classList.remove("opacity-100", "scale-100");
  toast.classList.add("opacity-0", "scale-95");
  setTimeout(() => {
    toast.classList.add("hidden");
  }, 300);
}

async function submitCartForm(e, form) {
  e.preventDefault();
  const url = form.action;
  const formData = new FormData(form);
  
  // Намираме картинката, независимо дали е в карта или модал
  let image = form.closest(".p-4")?.previousElementSibling?.querySelector("img");
  if (!image) {
    image = form.closest(".flex-1")?.previousElementSibling?.querySelector("img");
  }
  flyToCart(image);

  const response = await fetch(url, {
    method: "POST",
    headers: {
      'X-Requested-With': 'XMLHttpRequest'
    },
    body: formData
  });

  if (response.ok) {
    const data = await response.json();
    showToast("Продуктът е добавен в количката!");
    if (data.cart_count !== undefined) {
      updateCartCount(data.cart_count);
    }
  } else {
    showToast("❌ Грешка при добавяне!");
  }
  return false;
}

function flyToCart(imgElement) {
  if (!imgElement) return;
  const cartIcon = document.getElementById("cart-icon");
  const imgRect = imgElement.getBoundingClientRect();
  const cartRect = cartIcon.getBoundingClientRect();
  const flyingImg = imgElement.cloneNode(true);
  flyingImg.classList.add("flying-img");
  flyingImg.style.top = imgRect.top + "px";
  flyingImg.style.left = imgRect.left + "px";
  flyingImg.style.width = imgRect.width + "px";
  flyingImg.style.height = imgRect.height + "px";
  document.body.appendChild(flyingImg);
  requestAnimationFrame(() => {
    flyingImg.style.transform = `translate(${cartRect.left - imgRect.left}px, ${cartRect.top - imgRect.top}px) scale(0.1)`;
    flyingImg.style.opacity = "0";
  });
  setTimeout(() => flyingImg.remove(), 700);
  }
  function prevImage(productId) {
    const imgs = window.productImages[productId];
    let index = window.currentImageIndex[productId];

    index = (index - 1 + imgs.length) % imgs.length;
    window.currentImageIndex[productId] = index;

    const imgEl = document.getElementById(`product-image-${productId}`);
    imgEl.src = imgs[index];
  }

  function nextImage(productId) {
    const imgs = window.productImages[productId];
    let index = window.currentImageIndex[productId];

    index = (index + 1) % imgs.length;
    window.currentImageIndex[productId] = index;

    const imgEl = document.getElementById(`product-image-${productId}`);
    imgEl.src = imgs[index];
  }

  function openLightbox(url) {
    // Можеш да добавиш lightbox функция тук, ако искаш да отваря голяма снимка
    // Пример: show modal, insert url into <img>
  }
  document.addEventListener("click", function (event) {
    // Проверка дали кликваме върху модалния overlay
    const modalOverlay = event.target.closest("[id^='modal-']");
    if (!modalOverlay) return;
  
    const modalContent = modalOverlay.querySelector("[id^='modal-content-']");
    if (!modalContent) return;
  
    // Ако кликът е извън съдържанието на модала, затваряме
    if (!modalContent.contains(event.target)) {
      const productId = modalOverlay.dataset.modalId;
      closeModal(productId);
    }
  });

  document.getElementById('menu-toggle').addEventListener('click', function () {
    const menu = document.getElementById('mobile-menu');
    menu.classList.toggle('hidden');
  });


  
