
# FilmSearch

<h4>Description</h4>
API for searching through a collection of Netflix Movies and TV shows by Genre, Type, Cast or Title by keyword.

<h4>How to use the API</h4>

<h5>Search by Genre</h5>
https://filmsearch.tv/genre/*horror*

<h5>Search by Cast</h5>
https://filmsearch.tv/cast/*smith*

<h5>Search by Type</h5>
https://filmsearch.tv/type/*movie*

<h5>Search by Title</h5>
https://filmsearch.tv/title/*stranger*

<h5>Important Notes</h5>
    - The search query cannot be blank - this will return a 404
    - Partial searches will return anything that contains the string - eg. *hor* in genre will return horror.
    - This is a static dataset which is not continuously updated - new shows may not appear