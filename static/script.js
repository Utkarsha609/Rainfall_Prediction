// let preveiwContainer = document.querySelector("#graphs-preview");
let preveiwContainer = document.getElementById("graphs-preview");
let previewBox = preveiwContainer.querySelectorAll(".preview");

document.querySelectorAll(".graphs-container .graph").forEach((graph) => {
  graph.onclick = () => {
    preveiwContainer.style.display = "flex";
    let name = graph.getAttribute("data-name");
    previewBox.forEach((preview) => {
      let target = preview.getAttribute("data-target");
      if (name == target) {
        preview.classList.add("active");
      }
    });
  };
});

previewBox.forEach((close) => {
  close.querySelector(".fa-times").onclick = () => {
    close.classList.remove("active");
    preveiwContainer.style.display = "none";
  };
});
