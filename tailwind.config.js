/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./themes/**/*.html",
    "./themes/**/*.js",
    "./content/**/*.md"
  ],
  theme: {
    extend: {
      fontFamily: {
        'marble': ['Marble', 'cursive']
      },
      colors: {
        'shovels': {
          'primary': '#01654D',
          'secondary': '#E9BE51',
          'dark': '#101727',
          'light': '#EAE2CF'
        }
      }
    },
  },
  plugins: [
    require('@tailwindcss/forms'),
    require('@tailwindcss/line-clamp'),
  ],
};