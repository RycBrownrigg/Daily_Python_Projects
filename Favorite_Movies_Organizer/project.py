# Initial list of favorite movies
favorite_movies = ["Inception", "The Matrix", "Interstellar", "The Dark Knight"]

# Step 1: Add a new movie to the list (e.g., “The Godfather”).
favorite_movies.append("The Godfather")

# Step 2: Remove a specific movie from the list (e.g., “The Matrix”).
favorite_movies.remove("The Matrix")

# Step 3: Prints out the total number of movies in the list.
total_movies = len(favorite_movies)
print(f"Total number of movies: {total_movies}")

# Step 4: Sort the list alphabetically
favorite_movies.sort()

# Step 5: Print out the movies in alphabetical order
print("Your favorite movies in alphabetical order:")
for movie in favorite_movies:
    print(f"- {movie}")
