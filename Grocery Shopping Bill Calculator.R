#Grocery Shopping Bill Calculator

# Step 1: Create prices (change these numbers!)
prices <- c(250, 180, 450, 120, 300)          # Prices of 5 items in PKR
items  <- c("Rice", "Milk", "Oil", "Bread", "Eggs")

# Step 2: Calculate total
total <- sum(prices)
cat("Total before discount:", total, "PKR\n")

# Step 3: Simple discount rule (real shops do this!)
discount <- 0
if (total > 1000) {
  discount <- total * 0.10               # 10% off
  cat("Wow! You get 10% discount because total > 1000 PKR\n")
}

final_bill <- total - discount

# Step 4: Show nice message
cat("You bought:", paste(items, collapse = ", "), "\n")
cat("Final bill after discount:", final_bill, "PKR\n")
cat("You saved:", discount, "PKR \n")