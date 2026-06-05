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
          'primary': 'rgb(1 101 77 / <alpha-value>)',
          'secondary': '#E9BE51',
          'dark': '#101727',
          'light': '#EAE2CF'
        }
      },
      backgroundImage: {
        'gradient-radial': 'radial-gradient(var(--tw-gradient-stops))',
      },
      keyframes: {
        'logo-scroll': {
          from: { transform: 'translateX(0)' },
          to: { transform: 'translateX(-50%)' },
        },
      },
      animation: {
        'logo-scroll': 'logo-scroll var(--logo-scroll-duration, 40s) linear infinite',
      },
    },
  },
  plugins: [
    require('@tailwindcss/forms'),
    require('@tailwindcss/line-clamp'),
  ],
};