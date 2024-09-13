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
  ); // Error was here
  socket.onopen = function (e) {
    console.log("connection successfull");
  };
  socket.onclose = function (e) {
    console.log("not connected");
  };

  document.querySelector(".message-input").focus();
  // Submit message when pressing enter
  document.querySelector(".message-submit").onkeyup = function (e) {
    if (e.keyCode == 13) {
      // Enter = keyCode 13
      document.querySelector(".message-submit").click();
    }
  };
  // Submit onClick
  document.querySelector(".message-submit").onclick = function (e) {
    var message = document.querySelector(".message-input").value;
    console.log(message);
    // Send info to store it
    socket.send(
      JSON.stringify({
        message: message,
        username: "{{request.user.username}}",
      })
    );
  };

  socket.onmessage = function (e) {
    console.log("here");
    const data = JSON.parse(e.data);
    var div = document.createElement("div");
    div.innerHTML = data.username + " : " + data.message;
    document.querySelector(".message-input").value = "";
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
