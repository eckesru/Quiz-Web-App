function frageLiken(button) {
  var frageId = button.getAttribute("data-frage-id");
  var csrf_token = "{{ csrf_token }}";

  $.ajax({
    url: "like/",
    data: {
      frageId: frageId,
      csrfmiddlewaretoken: csrf_token,
    },
    dataType: "json",
    type: "POST",
    headers: {
      "X-CSRF-Token": csrf_token,
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
