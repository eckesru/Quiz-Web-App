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
