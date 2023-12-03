document.addEventListener("DOMContentLoaded", function() {
  function loadContent(url, targetElementId) {
    fetch(url)
      .then(response => response.text())
      .then(data => {
        var targetElement = document.getElementById(targetElementId);
        if (targetElement) {
          targetElement.innerHTML = data;
        } else {
          console.error('Error: Target element not found');
        }
      })
      .catch(error => console.error('Error:', error));
  }

  // Weitere Funktionen oder Code können hier stehen
});

console.log("paginator.js geladen");
