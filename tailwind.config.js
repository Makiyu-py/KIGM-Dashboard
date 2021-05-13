const colors = require('tailwindcss/colors');

module.exports = {
	purge: {
		enabled: process.env.NODE_ENV === 'production' ? true : false,
		content: ['./app/templates/**/*.html'],
	},
	darkMode: false, // or 'media' or 'class'
	theme: {
		extend: {},
	},
	colors: {
		gray: colors.blueGray,
	},
	variants: {
		extend: {},
	},
	plugins: [],
};
