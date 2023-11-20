function antwortLoeschen(frageId, antwortID) {
  var bestaetigung = confirm(
    "Bist du sicher, dass du diese Antwort löschen möchtest?"
  );
  if (bestaetigung) {
    // URL: frage/ID/antwort/ID/delete/
    window.location.href =
      "/frage/" + frageId + "/antwort/" + antwortID + "/delete/";
  }
}
