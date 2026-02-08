/* =========================
   CURSOR SYSTEM
========================= */
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


/* Cursor reactions */
document.addEventListener("mouseover", e => {
  if (
    e.target.tagName === "BUTTON" ||
    e.target.tagName === "INPUT" ||
    e.target.tagName === "TEXTAREA" ||
    e.target.closest(".cluster-bar")
  ) {
    ring.style.transform = "scale(1.8)";
  }
});

document.addEventListener("mouseout", e => {
  if (
    e.target.tagName === "BUTTON" ||
    e.target.tagName === "INPUT" ||
    e.target.tagName === "TEXTAREA" ||
    e.target.closest(".cluster-bar")
  ) {
    ring.style.transform = "scale(1)";
  }
});

/* =========================
   COMMENT SYSTEM
========================= */
function postComment() {
  const name = document.getElementById("username");
  const text = document.getElementById("comment-input");
  const list = document.getElementById("comments-list");

  if (!name.value.trim() || !text.value.trim()) {
    alert("Enter name and comment");
    return;
  }

  const div = document.createElement("div");
  div.className = "user-comment";
  div.innerHTML = `<strong>${name.value}</strong>${text.value}`;

  list.prepend(div);
  text.value = "";

  div.scrollIntoView({ behavior: "smooth" });
}

/* =========================
   SUMMARY TOGGLE
========================= */
function toggleSummary(e) {
  const summary = document.getElementById("summary-text");
  summary.classList.toggle("collapsed");

  e.target.innerText = summary.classList.contains("collapsed")
    ? "View More"
    : "View Less";
}
/* =========================
   COMMENT INSIGHTS ANIMATION
========================= */

document.querySelectorAll(".cluster-bar .fill").forEach(fill => {
  const width = fill.style.width;
  fill.style.setProperty("--target-width", width);
  fill.style.width = "0";

  setTimeout(() => {
    fill.style.width = width;
  }, 300);
});
