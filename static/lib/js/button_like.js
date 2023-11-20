function frageLiken(frageId) {
  var xhr = new XMLHttpRequest();
  xhr.onreadystatechange = function () {
    if (xhr.readyState === XMLHttpRequest.DONE) {
      if (xhr.status === 200) {
        var responseData = JSON.parse(xhr.responseText);
        var likeCountElement = document.getElementById("like-count");

        if (responseData.liked) {
          // Falls der Benutzer die Frage gemocht hat
          likeCountElement.innerText = parseInt(likeCountElement.innerText) + 1;
        } else {
          // Falls der Benutzer die Like zurückgenommen hat
          likeCountElement.innerText = parseInt(likeCountElement.innerText) - 1;
        }
      } else {
        console.error("Fehler beim Aktualisieren der Likes.");
      }
    }
  };

  // URL: frage/ID/like/

  //"frage/" + frageId + "/like"
  console.log("Frage ID:", frageId);
  xhr.open("POST", "test" + "/like", true);
  xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
  xhr.send("csrfmiddlewaretoken={{ csrf_token }}"); // Füge den CSRF-Token hinzu
}

/*
$(document).ready(function () {
  $("#like-button").click(function () {
    var frage_id = $(this).data("frage-id");
    $.ajax({
      url: "like/",
      data: {
        frage_id: frage_id,
      },
      dataType: "json",
      type: "POST",
      headers: {
        "X-CSRFToken": "{{ csrf_token }}",
      },
      success: function (response) {
        if (response.liked) {
          // Aktualisieren Sie hier die Anzeige, z.B. Like-Zähler oder Button-Stil
        }
      },
    });
  });
});
*/
