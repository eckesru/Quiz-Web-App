function frageLiken(frageId) {
  // Hier wird die Like-Funktion aufgerufen, wenn der Benutzer auf "Like" klickt
  $.ajax({
    //URL frage/ID/like/
    url: `/frage/${frageId}/like/`, // Die URL muss zur View führen, die die Like-Funktion enthält
    type: "POST", // Wir senden eine POST-Anfrage, da Likes Änderungen an den Daten vornehmen
    data: {}, // Hier könntest du zusätzliche Daten senden, wenn benötigt
    success: function (data) {
      // Der Server hat erfolgreich auf die Like-Anfrage reagiert
      if (data.liked) {
        // Der Benutzer hat die Frage geliked
        // Du kannst die Anzeige entsprechend aktualisieren
        updateLikeCount(frageId, data.liked);
      } else {
        // Der Benutzer hat den Like entfernt
        // Du kannst die Anzeige entsprechend aktualisieren
        updateLikeCount(frageId, data.liked);
      }
    },
    error: function (error) {
      // Es ist ein Fehler beim Senden der Like-Anfrage aufgetreten
      console.log("Fehler beim Senden des Like-Requests:", error);
    },
  });
}

// Funktion zum Aktualisieren der Like-Anzeige
function updateLikeCount(frageId, liked) {
  const likeCountElement = document.getElementById(
    `frage-like-count-${frageId}`
  );

  if (likeCountElement) {
    const currentLikes = parseInt(likeCountElement.innerText, 10);

    // Je nachdem, ob der Benutzer geliked oder den Like entfernt hat,
    // aktualisieren wir die Like-Anzeige entsprechend
    likeCountElement.innerText = liked ? currentLikes + 1 : currentLikes - 1;
  }
}
