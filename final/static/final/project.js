document.addEventListener("DOMContentLoaded", () => {
  // Navbar
  nav = document.querySelector(".nav");
  nav.style.display = "none";
  // Carousel
  const slides = document.querySelectorAll(".carousel-img");
  const titles = document.querySelectorAll(".carousel-title");
  slides[0].classList.add("active");
  titles[0].classList.add("active");

  document.querySelector(".prev").addEventListener("click", (e) => {
    prevSlide(slides, titles);
  });
  document.querySelector(".next").addEventListener("click", (e) => {
    nextSlide(slides, titles);
  });

  // Chat
  // Scroll bar on the bottom
  var messageBox = document.querySelector("#message-box");
  messageBox.scrollTop = messageBox.scrollHeight - messageBox.clientHeight;
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
    id = input.getAttribute("data-id");
    var message = input.value;

    fetch("/save", {
      method: "POST",
      body: JSON.stringify({ id, message }),
    }).then((res) => res.json());
    // Send info
    socket.send(
      JSON.stringify({
        message: message,
        id: id,
        username: user,
      })
    );
  };

  socket.onmessage = function (e) {
    const data = JSON.parse(e.data);
    var div = document.createElement("div");
    div.classList.add("messages");
    div.innerHTML = data.username + " : " + data.message;
    input.value = "";
    document.querySelector("#message-box").appendChild(div);
    // set the scrollbar to the bottom again
    messageBox.scrollTop = messageBox.scrollHeight - messageBox.clientHeight;
  };
});

// Carousel
let index = 0;
function prevSlide(slides, titles) {
  slides[index].classList.remove("active");
  titles[index].classList.remove("active");
  index--;

  if (index < 0) index = slides.length - 1;

  slides[index].classList.add("active");
  titles[index].classList.add("active");
}

function nextSlide(slides, titles) {
  slides[index].classList.remove("active");
  titles[index].classList.remove("active");
  index++;

  if (index > slides.length - 1) index = 0;

  slides[index].classList.add("active");
  titles[index].classList.add("active");
}
//
