 /*
 // Formular zum Fragen erstellen abrufen
const frageErstellenFormular = document.getElementById(
  "frageErstellenFormular"
);
const frageSpeichernButton = document.getElementById("frageSpeichernButton");

// Event-Handler für das Speichern der Frage
frageSpeichernButton.addEventListener("click", function () {
  // Die eingegebenen Werte abrufen
  const frageTitel = document.getElementById("frageTitel").value;
  var frageText = tinymce.get("frageText").getContent();
  const frageTag = document.getElementById("frageTag").value;
  const frageModul = document.getElementById("frageModul").value;

  // Datum abfragen
  // const frageErstelldatum = new Date().toLocaleDateString();

  // Konsolenausgabe der eingegebenen Daten
  console.log("Fragetitel", frageTitel);
  console.log("Fragetext", frageText);
  console.log("Tag", frageTag);
  console.log("Modul", frageModul);
//()  console.log("Erstelldatum Frage", frageErstelldatum);

  //Daten an Django senden
  fetch("/FrageErstellen/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      frageTitel,
      frageText,
      frageTag,
      frageModul,
      //frageErstelldatum,
    }),
  })
    .then((response) => response.json())
    .then((data) => {
      // Erfolgsmeldung
      console.log(data);
    })
    .catch((error) => {
      // Fehlerbehandlung
      console.error("Fehler beim Senden der Daten", error);
    });
});
*/

document.addEventListener("DOMContentLoaded", function(){
  document.getElementById("frageSpeichernButton").addEventListener("click", function(e){
      const frageTitel = document.getElementById("frageTitel").value;
      var frageText = tinymce.get("frageText").getContent();
      const frageTag = document.getElementById("frageTag").value;
      const frageModul = document.getElementById("frageModul").value;
  });
});


// TinyMCE um aus dem Fragetext ein Rich Text Editor zu machen
tinymce.init({
  selector: "#frageText",
  plugins: "lists link",
  toolbar:
    "undo redo | formatselect | bold italic underline | numlist bullist | link",
  menubar: false,
  width: "100%",
  height: 300,
});

// Prüfung ob JavaScript vollständig geladen wurde
console.log("frage.js wurde geladen.");
