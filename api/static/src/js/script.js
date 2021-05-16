const responsiveBtn = document.querySelector('.mobile-btn');
const headers = document.querySelectorAll('.resp-header');

responsiveBtn.addEventListener('click', () => {
	for (let i = 0; i < headers.length; i++) {
		headers[i].classList.toggle('hidden');
	}
});
