function loadContent(url, targetElementId) {
  fetch(url)
    .then((response) => response.text())
    .then((data) => {
      document.getElementById(targetElementId).innerHTML = data;
    })
    .catch((error) => console.error("Error:", error));
}
