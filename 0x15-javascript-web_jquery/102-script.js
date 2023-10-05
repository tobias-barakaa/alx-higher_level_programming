$(document).ready(function() {
    function fetchTranslation() {
        var languageCode = $("#language_code").val();
        $.get(`https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`, function(data) {
            var translation = data.hello;
            $("#hello").text(translation);
        });
    }
    $("#btn_translate").click(fetchTranslation);
    $("#language_code").keypress(function(e) {
        if (e.which == 13) {
            fetchTranslation();
        }
    });
});

