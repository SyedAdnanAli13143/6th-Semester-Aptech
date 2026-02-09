
r<- floor(runif(1, min=0, max=101))
rr<-round(r, digits = 0)
i <- 1
while (i !=0) {
 
  n<- as.numeric(readline(prompt = "Enter no :"))
  
  if (n>rr) {
    print("Too High")
  }else if (n<rr) {
    print("Too Low")
  }
  else if (n==rr) {
   
    print("W")
    paste("You tried  ", i, "and guess true number ",rr)
    break;
  }
  i <- i + 1
}


