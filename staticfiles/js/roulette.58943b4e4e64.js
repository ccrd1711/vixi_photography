document.addEventListener("DOMContentLoaded", function() {
  const images = document.querySelectorAll('.roulette-box img');
  let currentIndex = 0;

  setInterval(() => {
    images[currentIndex].classList.remove('active');
    currentIndex = (currentIndex + 1) % images.length;
    images[currentIndex].classList.add('active');
  }, 6500); // ~6.5 seconds
});
