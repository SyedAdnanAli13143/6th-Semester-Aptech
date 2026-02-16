# Clear screen (optional, for cleaner look)
{cat("\014")  # or use cat(rep("\n", 50)) if needed

cat("=== Movie Night Recommender ===\n")
cat("Enter 4 movies you watched recently!\n\n")

# Create empty vectors to store inputs
movie_names <- character(4)
ratings     <- numeric(4)

# Loop to get user inputs
for (i in 1:4) {
  cat("Movie", i, "name: ")
  movie_names[i] <- readline()
  
  cat("Your rating for", movie_names[i], "(out of 10): ")
  ratings[i] <- as.numeric(readline())
  
  # Simple check to avoid bad input (basic error handling)
  while (is.na(ratings[i]) || ratings[i] < 0 || ratings[i] > 10) {
    cat("Please enter a number between 0 and 10: ")
    ratings[i] <- as.numeric(readline())
  }
  cat("\n")
}

# Create data frame from inputs
movies <- data.frame(
  Name   = movie_names,
  Rating = ratings
)

# Show the list
cat("Your movie ratings:\n")
print(movies)

# Calculations
avg_rating  <- mean(movies$Rating)
best_rating <- max(movies$Rating)
best_movie  <- movies$Name[movies$Rating == best_rating]

# Results
cat("\nYour average rating:", round(avg_rating, 1), "/10\n")
cat("Tonight's recommendation:", best_movie, 
    "- your highest rated!", best_rating, "⭐\n")

# Fun personalized message
if (best_rating >= 8.5) {
  cat("This one is going to be epic! Grab popcorn 🍿🎥\n")
} else if (best_rating >= 7) {
  cat("Solid choice! Enjoy the movie 😊\n")
} else {
  cat("Hmm... maybe next time pick something higher rated 😉\n")
}
}
