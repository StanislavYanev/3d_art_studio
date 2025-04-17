
<script>
document.addEventListener("DOMContentLoaded", function () {
  let currentPage = 2;
  let loading = false;
  let hasMore = true;

  const gridContainer = document.querySelector("#gallery");
  const threshold = 200;

  async function loadMoreImages() {
    if (loading || !hasMore) return;
    loading = true;

    try {
      const response = await fetch(`/gallery/load-more/?page=${currentPage}`);
      const data = await response.json();

      if (data.images) {
        const tempDiv = document.createElement("div");
        tempDiv.innerHTML = data.images;
        const newImages = tempDiv.querySelectorAll("div");
        newImages.forEach(el => gridContainer.appendChild(el));
      }

      hasMore = data.has_next;
      currentPage++;
    } catch (error) {
      console.error("Грешка при зареждане на изображения:", error);
    } finally {
      loading = false;
    }
  }

  window.addEventListener("scroll", () => {
    if ((window.innerHeight + window.scrollY) >= (document.body.offsetHeight - threshold)) {
      loadMoreImages();
    }
  });
});
</script>
