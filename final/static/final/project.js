document.addEventListener("DOMContentLoaded", () => {
  nav = document.querySelector(".nav");
  nav.style.display = "none";
  const slides = document.querySelectorAll(".carousel-img");
  slides[0].classList.add("active");

  document.querySelector(".prev").addEventListener("click", (e) => {
    prevSlide(slides);
  });
  document.querySelector(".next").addEventListener("click", (e) => {
    nextSlide(slides);
  });
});

let index = 0;
function prevSlide(slides) {
  slides[index].classList.remove("active");
  index--;

  if (index < 0) index = slides.length - 1;

  slides[index].classList.add("active");
}

function nextSlide(slides) {
  slides[index].classList.remove("active");
  index++;

  if (index > slides.length - 1) index = 0;

  slides[index].classList.add("active");
}
