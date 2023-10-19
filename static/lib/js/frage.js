document.addEventListener("DOMContentLoaded", function(){
  document.getElementById("frageSpeichernButton").addEventListener("click", function(e){
      const frageTitel = document.getElementById("frageTitel").value;
      var frageText = tinymce.get("frageText").getContent();
      const frageTags = document.getElementById("frageTags").value;
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