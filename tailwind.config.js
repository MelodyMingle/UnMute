module.exports = {
  theme: {
    extend: {
      colors: {
        customOrange: '#EB9A2F',

  content: [
      './spottiapp/templates/**/*.html',
      './templates/**/*.html',
      './node_modules/flowbite/**/*.js'
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require('flowbite/plugin')
  ],
}