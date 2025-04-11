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
  (!localStorage.theme && window.matchMedia("(prefers-color-scheme: dark)").matches)
) {
  html.classList.add("dark");
}

updateThemeIcons();

themeToggle?.addEventListener("click", () => {
  html.classList.toggle("dark");
  localStorage.theme = html.classList.contains("dark") ? "dark" : "light";
  updateThemeIcons();
});
