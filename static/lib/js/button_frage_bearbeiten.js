function frageBearbeiten(frageId) {
  // URL: frage/ID/edit/
  window.location.href = "/frage/" + frageId + "/edit/";
}

document
  .getElementById("frageBearbeitenFormular")
  .addEventListener("submit", function (event) {
    var frageTextValue = tinymce.get("frageText").getContent();
    if (!frageTextValue.trim()) {
      alert("Bitte füllen Sie den Fragetext aus.");
      event.preventDefault(); // Verhindert das Absenden des Formulars
    }
  });
//console.log("button_frage_bearbeiten.js geladen")