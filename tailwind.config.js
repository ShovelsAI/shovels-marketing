/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./themes/**/*.html", "./themes/**/*.js"],
  theme: {
      extend: {
        fontFamily: {
          'marble': ['Marble', 'cursive']
        },
      },
  },
  plugins: [],
  };