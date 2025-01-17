import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the movie data from CSV
def load_data(file_path="movies.csv"):
    df = pd.read_csv(file_path)
    return df

# Analyze the top-rated movies
def analyze_top_rated_movies(df, top_n=10):
    top_movies = df.nlargest(top_n, "Rating")
    print(f"\nTop {top_n} Rated Movies:")
    print(top_movies[["Title", "Year", "Rating"]])

# Plot the distribution of movie ratings
def plot_rating_distribution(df):
    plt.figure(figsize=(10, 6))
    sns.histplot(df["Rating"], bins=10, kde=True, color="skyblue")
    plt.title("Distribution of Movie Ratings")
    plt.xlabel("Rating")
    plt.ylabel("Frequency")
    plt.show()

# Plot genre popularity over time
def plot_genre_popularity_over_time(df):
    genre_by_year = df.groupby(["Year", "Genre"]).size().unstack(fill_value=0)
    genre_by_year.plot(kind="line", figsize=(12, 6), marker="o")
    plt.title("Genre Popularity Over Time")
    plt.ylabel("Number of Movies")
    plt.xlabel("Year")
    plt.legend(title="Genre")
    plt.show()

# Main execution

# Load data
df = load_data()

# Analyze top-rated movies
analyze_top_rated_movies(df, top_n=5)

# Plot the distribution of movie ratings
plot_rating_distribution(df)

# Plot genre popularity over time
plot_genre_popularity_over_time(df)