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

//console.log("antwort.js geladen")
