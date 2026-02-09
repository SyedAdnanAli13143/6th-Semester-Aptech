Step 1: Install and Load the readxl Package (Only Once)
In RStudio:

Go to Console (bottom-left pane) and run these two lines one by one:

install.packages("readxl")   # Run this only the first time (downloads the package)
library(readxl)              # Run this every new R session (loads it)

student_data <- read_excel("C:/Users/YourName/Documents/student_data.xlsx")

View(student_data)          # opens nice table view
head(student_data)          # shows first 6 rows
summary(student_data)       # basic statistics



# Step 1: Load the package (do this every session)
library(readxl)

# Step 2: Import the Excel file
# Change the path to YOUR actual file location
student_data <- read_excel("C:/Users/Syed/Documents/student_data.xlsx")

# Alternative: if file is in your current working folder
# student_data <- read_excel("student_data.xlsx")

# Step 3: Check it worked
View(student_data)              # nice viewer
head(student_data, 3)            # first 3 rows
glimpse(student_data)            # shows structure nicely (install dplyr if needed)
summary(student_data)            # min, max, mean etc.

# Bonus: Quick plot example (now that data is in R)
plot(student_data$Marks_Maths, student_data$Marks_Stats,
     main = "Maths vs Stats Marks",
     xlab = "Maths", ylab = "Statistics",
     pch = 19, col = "blue")

Common useful options for read_excel():

# Read specific sheet (by name or number)
student_data <- read_excel("student_data.xlsx", sheet = "Sheet1")      # name
# or
student_data <- read_excel("student_data.xlsx", sheet = 1)             # position

# Skip first 2 rows (if title or empty rows)
student_data <- read_excel("student_data.xlsx", skip = 2)

# Change column names manually (if headers are bad)
student_data <- read_excel("student_data.xlsx", col_names = FALSE)
colnames(student_data) <- c("Name", "Sem", "Math", "Stats", "City", "Player")

# Tell R what is missing (NA)
student_data <- read_excel("student_data.xlsx", na = c("", "NA", "missing", "-"))



my_file <- file.choose()           # popup to select file
student_data <- read_excel(my_file)

student_data <- read_excel("student_data.xlsx", col_types = c("text", "numeric", "numeric", "numeric", "text", "text"))

Want CSV instead? (easier & faster in future)Save Excel as .csv → use readr::read_csv("file.csv")
library(readr)
psl_data <- read_csv("C:/Users/Syed/Desktop/psl_batting_2025.csv")


