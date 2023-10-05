$(document).ready(function() {
    $.get("https://swapi-api.alx-tools.com/api/films/?format=json", function(data) {
        var movieTitles = data.results;
        var ulElement = $("#list_movies");
        for (var i = 0; i < movieTitles.length; i++) {
            var title = movieTitles[i].title;
            var liElement = $("<li>").text(title);
            ulElement.append(liElement);
        }
    });
});
