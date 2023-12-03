document.addEventListener("DOMContentLoaded", function () {
  // Event Listener für die Klicks auf die Paginator-Links
  var paginationLinks = document.querySelectorAll(".pagination a");

  paginationLinks.forEach(function (link) {
    link.addEventListener("click", function (event) {
      event.preventDefault();

      // Die URL des Links holen
      var pageUrl = link.getAttribute("href");

      // Ajax-Aufruf, um nur die aktualisierten Fragen zu laden
      loadUpdatedQuestions(pageUrl);
    });
  });

  // Funktion zum Laden der aktualisierten Fragen per Ajax
  function loadUpdatedQuestions(url) {
    var xhr = new XMLHttpRequest();
    xhr.open("GET", url, true);

    xhr.onload = function () {
      if (xhr.status >= 200 && xhr.status < 400) {
        // Die empfangenen Daten in ein HTML-Element einfügen
        var container = document.querySelector(".fragen");
        container.innerHTML = xhr.responseText;

        // Falls es zusätzliche JavaScript-Funktionen gibt, die nachgeladen wurden,
        // können sie hier aktiviert werden.

        // Optional: Nach oben scrollen
        window.scrollTo(0, 0);
      } else {
        console.error("Fehler beim Laden der Fragen");
      }
    };

    xhr.onerror = function () {
      console.error("Netzwerkfehler beim Laden der Fragen");
    };

    xhr.send();
  }
});
