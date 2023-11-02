document
  .getElementById("loeschen-button")
  .addEventListener("click", function () {
    document.getElementById("bestaetigungsBox").style.display = "block";
  });

document
  .getElementById("bestaetigen-button")
  .addEventListener("click", function () {
    // Hier kannst du den Code für die Lösch-Aktion einfügen
    document.getElementById("bestaetigungsBox").style.display = "none";
    alert("Der Eintrag wurde gelöscht."); // Nur ein Beispiel-Alert
  });

document
  .getElementById("abbrechen-button")
  .addEventListener("click", function () {
    // Hier kannst du optionalen Code einfügen, wenn der Benutzer die Aktion abbricht
    document.getElementById("bestätigungsBox").style.display = "none";
    alert("Der Eintrag wurde nicht gelöscht.");
  });
