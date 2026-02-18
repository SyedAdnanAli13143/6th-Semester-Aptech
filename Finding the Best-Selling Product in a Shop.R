product <- c("Juice","Chips","Cookies","Juice","Chips","Cookies","Juice","Cookies","Chips","Juice")
quantity <- c(10,5,8,7,3,6,9,4,2,11)

sales <- data.frame(product, quantity)

sales

result <- aggregate(quantity ~ product, sales, sum)
result
barplot(result$quantity,
        names.arg=result$product,
        col="skyblue",
        main="Total Sales by Product")

