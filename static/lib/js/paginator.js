document.addEventListener("DOMContentLoaded", function () {
  function loadContent(url, targetElementId) {
    fetch(url)
      .then((response) => response.text())
      .then((data) => {
        // Überprüfe, ob das Element existiert, bevor du den Inhalt aktualisierst
        var targetElement = document.getElementById(targetElementId);
        if (targetElement) {
          targetElement.innerHTML = data;
        } else {
          console.error("Error: Target element not found");
        }
      })
      .catch((error) => console.error("Error:", error));
  }
});

console.log("paginator.js geladen");
