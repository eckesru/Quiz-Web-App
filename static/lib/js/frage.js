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

document
  .getElementById("frageErstellenFormular")
  .addEventListener("submit", function (event) {
    var frageTextValue = tinymce.get("frageText").getContent();
    if (!frageTextValue.trim()) {
      alert("Bitte füllen Sie den Fragetext aus.");
      event.preventDefault(); // Verhindert das Absenden des Formulars
    }
  });

//console.log("frage.js geladen")
