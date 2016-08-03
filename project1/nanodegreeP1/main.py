import fresh_tomatoes
import media
import entertainment_center


# Generates list of movie objects
movies = [entertainment_center.pulp_fiction,
          entertainment_center.the_hateful_eight,
          entertainment_center.django_unchained,
          entertainment_center.reservoir_dogs,
          entertainment_center.inglourious_basterds,
          entertainment_center.jackie_brown,
          entertainment_center.death_proof,
          entertainment_center.from_dusk_till_dawn]

# Instantiates fresh tomatoes html page builder
fresh_tomatoes.open_movies_page(movies)
