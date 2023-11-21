function frageLoeschen(frageId) {
  var bestaetigung = confirm(
    "Bist du sicher, dass du diese Frage löschen möchtest?"
  );
  if (bestaetigung) {
    // URL: frage/ID/delete/
    window.location.href = "/frage/" + frageId + "/delete/";
  }
}

//console.log("button_frage_loeschen.js geladen")