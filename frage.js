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
    const frageErstelldatum = new Date().toLocaleDateString();
    
    // Konsolenausgabe der eingegebenen Daten
    console.log("Fragetitel", frageTitel);
    console.log("Fragetext", frageText);
    console.log("Tag", frageTag);
    console.log("Modul", frageModul);
    console.log("Erstelldatum Frage", frageErstelldatum);
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