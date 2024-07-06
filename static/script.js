document
    .getElementById("search-form")
    .addEventListener("submit", function (event) {
        event.preventDefault();
        let title = document.getElementById("title").value;
        fetch("/search", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ title: title }),
        })
            .then((response) => response.json())
            .then((data) => {
                let searchResults = document.getElementById("search-results");
                searchResults.innerHTML =
                    "<h2>Search Results:</h2><ul>" +
                    data
                        .map(
                            (movie) =>
                                `<li>${movie.title} (${movie.genres})</li>`
                        )
                        .join("") +
                    "</ul>";
                let firstMovieId = data[0].movieId;
                fetch("/recommend", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify({ movie_id: firstMovieId }),
                })
                    .then((response) => response.json())
                    .then((recommendations) => {
                        let recommendationsDiv =
                            document.getElementById("recommendations");
                        console.log(recommendations);
                        recommendationsDiv.innerHTML =
                            "<h2>Recommended Movies:</h2><ul>" +
                            recommendations
                                .map(
                                    (movie) =>
                                        `<li>${movie.title} (${movie.genres})</li>`
                                )
                                .join("") +
                            "</ul>";
                    });
            });
    });
