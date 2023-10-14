const fehlermeldung = document.getElementById("fehlermeldung");
const erfolgsmeldung = document.getElementById("erfolgsmeldung");

// Fehlgeschlagene Anmeldung
fehlermeldung.textContent =
  "Login fehlgeschlagen. Bitte überprüfe deine Eingaben.";

// Erfolgreiche Anmeldung
erfolgsmeldung.textContent = "Login erfolgreich!";

// Zeige oder verstecke die Meldungen je nach Bedarf
function zeigeFehlermeldung() {
  fehlermeldung.style.display = "block";
  erfolgsmeldung.style.display = "none";
}

function zeigeErfolgsmeldung() {
  fehlermeldung.style.display = "none";
  erfolgsmeldung.style.display = "block";
}

// Event-Listener für das Login-Formular hinzufügen
document
  .getElementById("loginFormular")
  .addEventListener("submit", function (event) {
    event.preventDefault();

    //Login
    const email = document.getElementById("email").value;
    const passwort = document.getElementById("passwort").value;

    // Provisorische Prüfung des Logins
    if (email === "example@example.com" && passwort === "password123") {
      // Erfolgreiche Anmeldung
      console.log("Login erfolgreich!");
      zeigeErfolgsmeldung();

      // Weiterleitung zur frage.html nach einer kurzen Verzögerung
      setTimeout(function () {
        window.location.href = "frage.html";
      }, 2000); // 2000 Millisekunden (2 Sekunden) Verzögerung
    } else {
      // Fehlgeschlagene Anmeldung
      zeigeFehlermeldung();
    }
  });

// Prüfung ob JavaScript vollständig geladen wurde
console.log("frage.js wurde geladen.");
