// TinyMCE um aus dem Antworttext ein Rich Text Editor zu machen
tinymce.init({
  selector: "#antwortText",
  plugins: "lists link",
  toolbar:
    "undo redo | formatselect | bold italic underline | numlist bullist | link",
  menubar: false,
  width: "100%",
  height: 300,
});

document
  .getElementById("antwortErstellenFormular")
  .addEventListener("submit", function (event) {
    var frageTextValue = tinymce.get("antwortText").getContent();
    if (!frageTextValue.trim()) {
      alert("Bitte füllen Sie den Antworttext aus.");
      event.preventDefault(); // Verhindert das Absenden des Formulars
    }
  });

//console.log("antwort.js geladen")
