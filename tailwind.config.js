/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./themes/**/*.html", "./themes/**/*.js", "./content/**/*.md"],
  theme: {
    extend: {
      fontFamily: {
        'marble': ['Marble', 'cursive']
      },
    },
  },
  plugins: [
    require('@tailwindcss/forms'),
  ],
};