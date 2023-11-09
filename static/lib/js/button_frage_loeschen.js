function bestaetigeLoeschen(frageId) {
  var bestaetigung = confirm(
    "Bist du sicher, dass du diese Frage löschen möchtest?"
  );
  if (bestaetigung) {
    window.location.href = "/frage/" + frageId + "/delete/";
  }
}
