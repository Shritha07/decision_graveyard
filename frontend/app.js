async function loadTimeline() {
  const res = await fetch("http://127.0.0.1:5002/decisions");
  const data = await res.json();

  const timeline = document.getElementById("timeline");
  timeline.innerHTML = "";

  data.forEach(d => {
    timeline.innerHTML += `
      <div class="timeline-card">
        <strong>${d.title}</strong><br>
        <small>${d.date}</small>
        <p>${d.taken_path}</p>
        <em>${d.reflection}</em>
      </div>
    `;
  });
}
async function saveDecision() {
  await fetch("http://127.0.0.1:5002/decisions", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({
      title: title.value,
      date: date.value,
      taken_path: path.value,
      reflection: reflection.value,
      mood: 3
    })
  });
  loadTimeline();
}

loadTimeline();
