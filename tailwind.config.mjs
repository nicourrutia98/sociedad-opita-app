/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,js,jsx,ts,tsx,md,mdx}'],
  theme: {
    extend: {
      colors: {
        // Paleta del opita — extraída de web/style.css del protito
        opita: {
          tierra: '#6b3e2e',     // marrón principal (skin, adobe)
          adobe: '#a87856',      // adobe claro
          arena: '#faf6ed',      // arena, papel viejo
          hueso: '#d7ccc8',      // hueso, beige claro
          cafe: '#2c1810',       // café muy oscuro, casi negro
          plaza: '#b8d4a0',      // verde plaza
          magdalena: '#6892b0',  // azul río Magdalena
          verriondo: '#8b5a3c',  // color cálido para acentos
        },
      },
      fontFamily: {
        serif: ['Georgia', 'serif'],
        sans: ['system-ui', '-apple-system', 'sans-serif'],
      },
      typography: {
        DEFAULT: {
          css: {
            color: 'var(--color-opita-cafe)',
          },
        },
      },
    },
  },
  plugins: [],
};
