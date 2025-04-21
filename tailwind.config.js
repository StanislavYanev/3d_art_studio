/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './**/templates/**/*.html',
    './templates/**/*.html',
    './**/*.js', 
  ]
  darkMode: 'class',
  theme: {
    extend: {
      fontFamily: {
        josefin: ['"Josefin Sans"', 'sans-serif'],
        quicksand: ['"Quicksand"', 'sans-serif'],
      },
    },
  },
  plugins: [],
}
