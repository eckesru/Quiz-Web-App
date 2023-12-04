function submitAntwort() {
  // Ausgewählte Antwort abrufen
  var questionId = document
    .getElementById("PruefenButton")
    .getAttribute("data-question-id");
  var userAnswer = document.querySelector(
    'input[name="answer_' + questionId + '"]:checked'
  );

  if (!userAnswer) {
    // Der Benutzer hat keine Antwort ausgewählt
    alert("Bitte wähle eine Antwort aus.");
    preventDefault();
  }

  // Hier überprüfen, ob der Benutzer bereits geantwortet hat
  //if ("{{ answer_user_frage_des_tages }}" !== "") {
    //alert("Du hast bereits geantwortet!");
    //preventDefault();
  //}

  // Formular-Daten vorbereiten
  var formData = new FormData(document.getElementById("antwort-form"));
  formData.append("user_answer", userAnswer.value);

  // AJAX-Anfrage senden
  fetch("{% url 'antwort-einreichen' %}", {
    method: "POST",
    body: formData,
    credentials: "same-origin",
    headers: {
      "X-CSRFToken": getCookie("csrftoken"), // CSRF-Token hinzufügen
    },
  })
    .then((response) => response.json())
    .then((data) => {
      // Daten verarbeiten, je nach Bedarf
      if (data.allowed) {
        // Erfolgreich durchgeführt
        console.log("Aktion erfolgreich durchgeführt");
      } else {
        // Aktion wurde nicht durchgeführt
        console.log("Aktion nicht durchgeführt");
      }
    })
    .catch((error) => {
      console.error("Fehler bei der Anfrage:", error);
    });
}

// Funktion, um das CSRF-Token aus den Cookies zu erhalten
function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    var cookies = document.cookie.split(";");
    for (var i = 0; i < cookies.length; i++) {
      var cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
