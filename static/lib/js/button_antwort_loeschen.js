function antwortloeschen(frageId, antwortID) {
  // URL: frage/ID/antwort/ID/delete/
  window.location.href =
    "/frage/" + frageId + "antwort" + antwortID + "/delete/";
}
