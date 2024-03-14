module.exports = {
  content: [
      './spottiapp/templates/**/*.html',
      './templates/**/*.html',
      './node_modules/flowbite/**/*.js'
  ],
  theme: {
    extend: {
      colors: {
        'primary': '#2C032C', // deep purple
        'secondary': '#691370', // mid purple
        'tertiary': '#DCD0C4', // cream
        'quaternary': '#C922AE', // pink
        'quinary': '#EB9A2F', // orange
        'senary': '#3F0140', // dark purple
        'septenary': '#FFA500',
        'octonary': '#FFD700',
        'nonary': '#FFA500',
        'denary': '#FFD700',
      },
    },
  },
  plugins: [
    require('flowbite/plugin')
  ],
}