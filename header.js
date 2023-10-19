document.addEventListener("DOMContentLoaded", function () {
  const loggedInUser = localStorage.getItem("loggedInUser");
  const loggedInStatusElement = document.getElementById("loggedInStatus");
  const logoutButton = document.getElementById("logoutButton");

  function updateLoggedInStatus() {
    if (loggedInUser) {
      // Der Benutzer ist angemeldet
      loggedInStatusElement.textContent = "Angemeldet als " + loggedInUser;
      logoutButton.style.display = "block"; // Zeige die Logout-Schaltfläche
    } else {
      // Der Benutzer ist nicht angemeldet
      loggedInStatusElement.textContent = "Nicht angemeldet";
      logoutButton.style.display = "none"; // Verstecke die Logout-Schaltfläche
    }
  }

  // Initialen Benutzerstatus festlegen
  updateLoggedInStatus();

  // Logout-Funktion
  logoutButton.addEventListener("click", function () {
    localStorage.removeItem("loggedInUser");
    window.location.href = "login.html";
  });
});
