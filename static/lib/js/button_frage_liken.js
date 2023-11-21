function frageLiken(frageId) {
  // CSRF-Token abrufen
  const csrftoken = getCookie("csrftoken");

  // Hier wird die Like-Funktion aufgerufen, wenn der Benutzer auf "Like" klickt
  $.ajax({
    //URL: frage/ID/like/
    url: `/frage/${frageId}/like/`,
    type: "POST",
    headers: { "X-CSRFToken": csrftoken },
    data: {}, // Hier könnten zusätzliche Daten gesendet werden, wenn benötigt
    success: function (data) {
      // Der Server hat erfolgreich auf die Like-Anfrage reagiert
      if (data.liked) {
        // Der Benutzer hat die Frage geliked
        updateLikeCount(frageId, data.liked);
      } else {
        // Der Benutzer hat den Like entfernt
        updateLikeCount(frageId, data.liked);
      }
    },
    error: function (error) {
      // Es ist ein Fehler beim Senden der Like-Anfrage aufgetreten
      console.log("Fehler beim Senden des Like-Requests:", error);
    },
  });
}

// CSRF-Token aus den Cookies abrufen
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

// Funktion zum Aktualisieren der Like-Anzeige
function updateLikeCount(frageId, liked) {
  const likeCountElement = document.getElementById(
    `frage-like-count-${frageId}`
  );

  if (likeCountElement) {
    const currentLikes = parseInt(likeCountElement.innerText, 10);

    // Je nachdem, ob der Benutzer geliked oder den Like entfernt hat, aktualisieren wir die Like-Anzeige entsprechend
    likeCountElement.innerText = liked ? currentLikes + 1 : currentLikes - 1;
  }
}

//console.log("button_frage_like geladen");
