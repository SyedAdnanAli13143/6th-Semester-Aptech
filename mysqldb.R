con<-dbConnect(MySQL(),
               username = "root",
               dbname = "rstudiodb"
               
               )
dbListTables(con)
dbListFields(con,"rtb")

dataview<-dbGetQuery(con,"Select * from rtb")
View(dataview)
print(dataview)

d<-dbSendQuery(con,"Select * from rtb")
# error view(d)
data<-fetch(d,n=-1)
View(data)
