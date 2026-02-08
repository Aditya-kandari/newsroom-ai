const cursor = document.createElement("div");
const ring = document.createElement("div");

cursor.classList.add("cursor");
ring.classList.add("cursor-ring");

document.body.appendChild(cursor);
document.body.appendChild(ring);

function goArticles() {
  window.location.href = "articles.html";
}


document.addEventListener("mousemove", (e) => {
  cursor.style.left = e.clientX + "px";
  cursor.style.top = e.clientY + "px";

  ring.style.left = e.clientX + "px";
  ring.style.top = e.clientY + "px";
});
