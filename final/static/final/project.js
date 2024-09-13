document.addEventListener("DOMContentLoaded", () => {
  // Navbar
  nav = document.querySelector(".nav");
  nav.style.display = "none";
  // Carousel
  const slides = document.querySelectorAll(".carousel-img");
  slides[0].classList.add("active");

  document.querySelector(".prev").addEventListener("click", (e) => {
    prevSlide(slides);
  });
  document.querySelector(".next").addEventListener("click", (e) => {
    nextSlide(slides);
  });

  // Chat
  // Create a new Websocket
  const socket = new WebSocket(
    "ws://" + window.location.href.replace(/^http(s?):\/\//i, "")
  );
  socket.onopen = function (e) {
    console.log("connection successfull");
  };
  socket.onclose = function (e) {
    console.log("not connected");
  };

  input = document.querySelector(".message-input");
  submit = document.querySelector(".message-submit");
  input.focus();
  // Submit message when pressing enter
  submit.onkeyup = function (e) {
    if (e.keyCode == 13) {
      // Enter = keyCode 13
      submit.click();
    }
  };
  // Submit onClick
  user = input.getAttribute("data-user");
  submit.onclick = function (e) {
    var message = input.value;
    // Send info
    socket.send(
      JSON.stringify({
        message: message,
        username: user,
      })
    );
  };

  socket.onmessage = function (e) {
    const data = JSON.parse(e.data);
    var div = document.createElement("div");
    div.innerHTML = data.username + " : " + data.message;
    input.value = "";
    document.querySelector("#message-box").appendChild(div);
  };
});


// Carousel
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
//
