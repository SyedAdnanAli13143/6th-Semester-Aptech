#Student Marks Report Card

# Your marks in 5 subjects (change these!)
math     <- 78
english  <- 65
science  <- 92
urdu     <- 55
computer <- 88

# Put in a data frame (like Excel table)
marks <- data.frame(
  Subject = c("Math", "English", "Science", "Urdu", "Computer"),
  Score   = c(math, english, science, urdu, computer)
)

# Calculate total and percentage
total_marks <- sum(marks$Score)
percentage  <- (total_marks / 500) * 100

# Simple grade logic
grade <- "F"
if (percentage >= 90) grade <- "A+"
if (percentage >= 80 & percentage < 90) grade <- "A"
if (percentage >= 70 & percentage < 80) grade <- "B"
if (percentage >= 60 & percentage < 70) grade <- "C"

# Show report
print(marks)
cat("\nTotal:", total_marks, "/500\n")
cat("Percentage:", round(percentage, 1), "%\n")
cat("Grade:", grade, "\n")

if (percentage >= 60) {
  cat("Congratulations! You PASSED \n")
} else {
  cat("Better luck next time. Keep studying! \n")
}