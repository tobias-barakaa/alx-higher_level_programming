(function() {
    $.get("https://hellosalut.stefanbohacek.dev/?lang=fr", function(data) {
      const hello = data.hello;
        $("#hello").text(hello);
    });
  })();
