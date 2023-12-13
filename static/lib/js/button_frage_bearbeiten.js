function frageBearbeiten(frageId) {
  // URL: frage/ID/edit/
  window.location.href = "/frage/" + frageId + "/edit/";
}

function istFrageTextBefuellt() {
  const frageText = document.getElementById('frageText').value;
  return frageText.length > 0;
}

//console.log("button_frage_bearbeiten.js geladen")