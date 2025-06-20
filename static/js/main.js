document.addEventListener('DOMContentLoaded', () => {
  // Sidebar toggle
  const sidebar  = document.getElementById('sidebar');
  const toggleBtn = document.getElementById('toggleBtn');
  toggleBtn.addEventListener('click', () => sidebar.classList.toggle('open'));
  document.addEventListener('keydown', e => {
    if (e.key === 'Tab') {
      e.preventDefault();
      sidebar.classList.toggle('open');
    }
  });

  // Carousel initializer
  function initSlider(sliderId, dotsId) {
    const slides = document.querySelectorAll(`#${sliderId} .slide`);
    const dotsContainer = document.getElementById(dotsId);
    let current = 0, interval;

    // Build dots
    slides.forEach((_, i) => {
      const dot = document.createElement('span');
      dot.className = 'dot' + (i === 0 ? ' active' : '');
      dot.addEventListener('click', () => {
        showSlide(i);
        resetAuto();
      });
      dotsContainer.appendChild(dot);
    });

    function showSlide(i) {
      slides[current].classList.remove('active');
      dotsContainer.children[current].classList.remove('active');
      current = i;
      slides[current].classList.add('active');
      dotsContainer.children[current].classList.add('active');
    }

    function autoAdvance() {
      showSlide((current + 1) % slides.length);
    }

    function resetAuto() {
      clearInterval(interval);
      interval = setInterval(autoAdvance, 10000);
    }

    // Start
    interval = setInterval(autoAdvance, 10000);
  }

  initSlider('choice-slider', 'choice-dots');
  initSlider('recs-slider',   'recs-dots');
});
