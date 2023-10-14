document
  .getElementById("loginFormular")
  .addEventListener("submit", function (event) {
    event.preventDefault();

    //Login
    const email = document.getElementById("email").value;
    const passwort = document.getElementById("passwort").value;

    // Prüfung des Logins (provisorisch)
    if (email === "example@example.com" && passwort === "password123") {
      // Erfolgreiche Anmeldung
      console.log("Erfolgreich eingeloggt!");

      // Weiterleitung zur index.html
      window.location.href = "frage.html";
    } else {
      // Fehlgeschlagene Anmeldung
      console.error("Login fehlgeschlagen. Bitte überprüfe deine Eingaben.");
    }
  });

// Prüfung ob JavaScript vollständig geladen wurde
console.log("frage.js wurde geladen.");
