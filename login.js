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

    /*
    // AJAX-Anfrage an das Django-Backend
    const url = "/auth/login/";  // Django-Authentifizierungs-URL an
    const data = {
        email: email,
        passwort: passwort
    };

    fetch(url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            // Erfolgreiche Anmeldung
            console.log("Login erfolgreich!");
            zeigeErfolgsmeldung();
            window.location.href = "frage.html";
        } else {
            // Fehlgeschlagene Anmeldung
            console.error("Anmeldung fehlgeschlagen. Bitte überprüfe deine Eingaben.");
            zeigeFehlermeldung();
        }
    })
    .catch(error => console.error("Fehler beim Senden der Anmeldeanfrage:", error));
});
    */

    // Provisorische Prüfung des Logins
    if (email === "example@example.com" && passwort === "password123") {
      // Erfolgreiche Anmeldung
      console.log("Login erfolgreich!");

      // Speichern der Anmeldeinformationen im localStorage
      localStorage.setItem("loggedInUser", email);

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
