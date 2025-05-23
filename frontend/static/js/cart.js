document.getElementById("open-cart")?.addEventListener("click", () => {
    document.getElementById("cart-modal")?.classList.remove("hidden");
    document.getElementById("cart-modal")?.classList.add("flex");
    fetch('/cart/', {
      headers: { "X-Requested-With": "XMLHttpRequest" }
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
        return fetch('/cart/', {
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
  
  function updateQuantity(productId, newQty) {
    if (newQty < 1) return;
  
    fetch(`/cart/update/${productId}/`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": getCSRFToken(),
        "X-Requested-With": "XMLHttpRequest"
      },
      body: JSON.stringify({ quantity: newQty })
    })
      .then(response => {
        if (response.ok) {
          // Презареди частта с количката (или страницата)
          return fetch('/cart/', {
            headers: { 'X-Requested-With': 'XMLHttpRequest' }
          });
        } else {
          console.error("Отговор от сървъра:", response.status);
        }
      })
      .then(res => res.text())
      .then(html => {
        document.getElementById("cart-content").innerHTML = html;
      })
      .catch(err => console.error("Грешка при заявка:", err));
  }
  