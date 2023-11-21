function antwortBearbeiten(frageId, antwortID) {
  // URL: frage/ID/antwort/ID/edit/
  window.location.href = "/frage/" + frageId + "/antwort/" + antwortID + "/edit/";
}

console.log("button_antwort_bearbeiten.js geladen")