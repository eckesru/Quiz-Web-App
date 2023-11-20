function frageLiken(button) {
  var frageId = button.getAttribute("data-frage-id");
  var csrf_token = "{{ csrf_token }}";

  $.ajax({
    url: "like/",
    data: {
      frageId: frageId,
    },
    dataType: "json",
    type: "POST",
    headers: {
      "X-CSRFToken": csrf_token,
    },
  })
    .done(function (response) {
      if (response.liked) {
        // Aktualisieren Sie hier die Anzeige, z.B. Like-Zähler oder Button-Stil
      }
    })
    .fail(function (xhr, status, error) {
      console.error("AJAX request failed:", status, error);
    });
}
