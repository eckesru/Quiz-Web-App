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
