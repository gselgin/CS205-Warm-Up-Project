library(dplyr)

setwd("C:/Users/skenn/Desktop/UVM/CS 205/Warm-Up Project/avocado.csv")
data = read.csv("avocado.csv", header = TRUE)

View(data)

data<-data%>%
  select(Date, AveragePrice, Total.Volume, type, region) %>%
  filter(region == "GreatLakes" | region == "HarrisburgScranton" | region == "HartfordSpringfield" | region == "Houston" | region == "Indianapolis" | region == "Jacksonville" | region == "LasVegas" | region == "LosAngeles" | region == "Louisville" | region == "MiamiFtLauderdale" | region == "MidSouth" | region == "Nashville" | region == "NewOrleansMobile" | region == "NewYork" | region == "Northeast" | region == "NorthernNewEngland")

data$Date<-as.Date(data$Date ,format="%Y-%m-%d")

##########################################################
december_con<-data %>%
  tbl_df() %>%
  select(Date, AveragePrice, Total.Volume, type, region) %>%
  filter(data$Date >= as.Date("2015-12-01") & data$Date < as.Date("2016-01-01") & type == "conventional")

december_con<-december_con%>%
  select(AveragePrice, Total.Volume, region) %>%
  group_by(region)%>%
  summarise_all(funs(mean))

december_con$Total.Volume<-december_con$Total.Volume*31

december_con$Date="2015-12"
december_con$type="conventional"

write.csv(december_con, "C:/Users/skenn/Desktop/UVM/CS 205/Warm-Up Project/december_con.csv")

december_org<-data %>%
  tbl_df() %>%
  select(Date, AveragePrice, Total.Volume, type, region) %>%
  filter(data$Date >= as.Date("2015-12-01") & data$Date < as.Date("2016-01-01") & type == "organic")

december_org<-december_org%>%
  select(AveragePrice, Total.Volume, region) %>%
  group_by(region)%>%
  summarise_all(funs(mean))

december_org$Total.Volume<-december_org$Total.Volume*31

december_org$Date="2015-12"
december_org$type="organic"

write.csv(december_org, "C:/Users/skenn/Desktop/UVM/CS 205/Warm-Up Project/december_org.csv")

##########################################################
november_con<-data %>%
  tbl_df() %>%
  select(Date, AveragePrice, Total.Volume, type, region) %>%
  filter(data$Date >= as.Date("2015-11-01") & data$Date < as.Date("2015-12-01") & type == "conventional")

november_con<-november_con%>%
  select(AveragePrice, Total.Volume, region) %>%
  group_by(region)%>%
  summarise_all(funs(mean))

november_con$Total.Volume<-november_con$Total.Volume*30

november_con$Date="2015-11"
november_con$type="conventional"

write.csv(november_con, "C:/Users/skenn/Desktop/UVM/CS 205/Warm-Up Project/november_con.csv")

november_org<-data %>%
  tbl_df() %>%
  select(Date, AveragePrice, Total.Volume, type, region) %>%
  filter(data$Date >= as.Date("2015-11-01") & data$Date < as.Date("2015-12-01") & type == "organic")

november_org<-november_org%>%
  select(AveragePrice, Total.Volume, region) %>%
  group_by(region)%>%
  summarise_all(funs(mean))

november_org$Total.Volume<-november_org$Total.Volume*30

november_org$Date="2015-11"
november_org$type="organic"

write.csv(november_org, "C:/Users/skenn/Desktop/UVM/CS 205/Warm-Up Project/november_org.csv")

##########################################################
october_con<-data %>%
  tbl_df() %>%
  select(Date, AveragePrice, Total.Volume, type, region) %>%
  filter(data$Date >= as.Date("2015-10-01") & data$Date < as.Date("2015-11-01") & type == "conventional")

october_con<-october_con%>%
  select(AveragePrice, Total.Volume, region) %>%
  group_by(region)%>%
  summarise_all(funs(mean))

october_con$Total.Volume<-october_con$Total.Volume*31

october_con$Date="2015-10"
october_con$type="conventional"

write.csv(october_con, "C:/Users/skenn/Desktop/UVM/CS 205/Warm-Up Project/october_con.csv")

october_org<-data %>%
  tbl_df() %>%
  select(Date, AveragePrice, Total.Volume, type, region) %>%
  filter(data$Date >= as.Date("2015-10-01") & data$Date < as.Date("2015-11-01") & type == "organic")

october_org<-october_org%>%
  select(AveragePrice, Total.Volume, region) %>%
  group_by(region)%>%
  summarise_all(funs(mean))

october_org$Total.Volume<-october_org$Total.Volume*31

october_org$Date="2015-10"
october_org$type="organic"

write.csv(october_org, "C:/Users/skenn/Desktop/UVM/CS 205/Warm-Up Project/october_org.csv")

##########################################################
september_con<-data %>%
  tbl_df() %>%
  select(Date, AveragePrice, Total.Volume, type, region) %>%
  filter(data$Date >= as.Date("2015-09-01") & data$Date < as.Date("2015-10-01") & type == "conventional")

september_con<-september_con%>%
  select(AveragePrice, Total.Volume, region) %>%
  group_by(region)%>%
  summarise_all(funs(mean))

september_con$Total.Volume<-september_con$Total.Volume*30

september_con$Date="2015-09"
september_con$type="conventional"

write.csv(september_con, "C:/Users/skenn/Desktop/UVM/CS 205/Warm-Up Project/september_con.csv")

september_org<-data %>%
  tbl_df() %>%
  select(Date, AveragePrice, Total.Volume, type, region) %>%
  filter(data$Date >= as.Date("2015-09-01") & data$Date < as.Date("2015-10-01") & type == "organic")

september_org<-september_org%>%
  select(AveragePrice, Total.Volume, region) %>%
  group_by(region)%>%
  summarise_all(funs(mean))

september_org$Total.Volume<-september_org$Total.Volume*30

september_org$Date="2015-09"
september_org$type="organic"

write.csv(september_org, "C:/Users/skenn/Desktop/UVM/CS 205/Warm-Up Project/september_org.csv")

##########################################################
august_con<-data %>%
  tbl_df() %>%
  select(Date, AveragePrice, Total.Volume, type, region) %>%
  filter(data$Date >= as.Date("2015-08-01") & data$Date < as.Date("2015-09-01") & type == "conventional")

august_con<-august_con%>%
  select(AveragePrice, Total.Volume, region) %>%
  group_by(region)%>%
  summarise_all(funs(mean))

august_con$Date="2015-08"
august_con$type="conventional"

august_con$Total.Volume<-august_con$Total.Volume*31

write.csv(august_con, "C:/Users/skenn/Desktop/UVM/CS 205/Warm-Up Project/august_con.csv")

august_org<-data %>%
  tbl_df() %>%
  select(Date, AveragePrice, Total.Volume, type, region) %>%
  filter(data$Date >= as.Date("2015-08-01") & data$Date < as.Date("2015-09-01") & type == "organic")

august_org<-august_org%>%
  select(AveragePrice, Total.Volume, region) %>%
  group_by(region)%>%
  summarise_all(funs(mean))

august_org$Total.Volume<-august_org$Total.Volume*31

august_org$Date="2015-08"
august_org$type="organic"

write.csv(august_org, "C:/Users/skenn/Desktop/UVM/CS 205/Warm-Up Project/august_org.csv")

##########################################################
july_con<-data %>%
  tbl_df() %>%
  select(Date, AveragePrice, Total.Volume, type, region) %>%
  filter(data$Date >= as.Date("2015-07-01") & data$Date < as.Date("2015-08-01") & type == "conventional")

july_con<-july_con%>%
  select(AveragePrice, Total.Volume, region) %>%
  group_by(region)%>%
  summarise_all(funs(mean))

july_con$Total.Volume<-july_con$Total.Volume*31

july_con$Date="2015-07"
july_con$type="conventional"

write.csv(july_con, "C:/Users/skenn/Desktop/UVM/CS 205/Warm-Up Project/july_con.csv")

july_org<-data %>%
  tbl_df() %>%
  select(Date, AveragePrice, Total.Volume, type, region) %>%
  filter(data$Date >= as.Date("2015-07-01") & data$Date < as.Date("2015-08-01") & type == "organic")

july_org<-july_org%>%
  select(AveragePrice, Total.Volume, region) %>%
  group_by(region)%>%
  summarise_all(funs(mean))

july_org$Total.Volume<-july_org$Total.Volume*31

july_org$Date="2015-07"
july_org$type="organic"

write.csv(july_org, "C:/Users/skenn/Desktop/UVM/CS 205/Warm-Up Project/july_org.csv")

##########################################################
june_con<-data %>%
  tbl_df() %>%
  select(Date, AveragePrice, Total.Volume, type, region) %>%
  filter(data$Date >= as.Date("2015-06-01") & data$Date < as.Date("2015-07-01") & type == "conventional")

june_con<-june_con%>%
  select(AveragePrice, Total.Volume, region) %>%
  group_by(region)%>%
  summarise_all(funs(mean))

june_con$Total.Volume<-june_con$Total.Volume*30

june_con$Date="2015-06"
june_con$type="conventional"

write.csv(june_con, "C:/Users/skenn/Desktop/UVM/CS 205/Warm-Up Project/june_con.csv")

june_org<-data %>%
  tbl_df() %>%
  select(Date, AveragePrice, Total.Volume, type, region) %>%
  filter(data$Date >= as.Date("2015-06-01") & data$Date < as.Date("2015-07-01") & type == "organic")

june_org<-june_org%>%
  select(AveragePrice, Total.Volume, region) %>%
  group_by(region)%>%
  summarise_all(funs(mean))

june_org$Total.Volume<-june_org$Total.Volume*30

june_org$Date="2015-06"
june_org$type="organic"

write.csv(june_org, "C:/Users/skenn/Desktop/UVM/CS 205/Warm-Up Project/june_org.csv")

##########################################################
may_con<-data %>%
  tbl_df() %>%
  select(Date, AveragePrice, Total.Volume, type, region) %>%
  filter(data$Date >= as.Date("2015-05-01") & data$Date < as.Date("2015-06-01") & type == "conventional")

may_con<-may_con%>%
  select(AveragePrice, Total.Volume, region) %>%
  group_by(region)%>%
  summarise_all(funs(mean))

may_con$Total.Volume<-may_con$Total.Volume*31

may_con$Date="2015-05"
may_con$type="conventional"

write.csv(may_con, "C:/Users/skenn/Desktop/UVM/CS 205/Warm-Up Project/may_con.csv")

may_org<-data %>%
  tbl_df() %>%
  select(Date, AveragePrice, Total.Volume, type, region) %>%
  filter(data$Date >= as.Date("2015-05-01") & data$Date < as.Date("2015-06-01") & type == "organic")

may_org<-may_org%>%
  select(AveragePrice, Total.Volume, region) %>%
  group_by(region)%>%
  summarise_all(funs(mean))

may_org$Total.Volume<-may_org$Total.Volume*31

may_org$Date="2015-05"
may_org$type="organic"

write.csv(may_org, "C:/Users/skenn/Desktop/UVM/CS 205/Warm-Up Project/may_org.csv")

##########################################################
april_con<-data %>%
  tbl_df() %>%
  select(Date, AveragePrice, Total.Volume, type, region) %>%
  filter(data$Date >= as.Date("2015-04-01") & data$Date < as.Date("2015-05-01") & type == "conventional")

april_con<-april_con%>%
  select(AveragePrice, Total.Volume, region) %>%
  group_by(region)%>%
  summarise_all(funs(mean))

april_con$Total.Volume<-april_con$Total.Volume*30

april_con$Date="2015-04"
april_con$type="conventional"

write.csv(april_con, "C:/Users/skenn/Desktop/UVM/CS 205/Warm-Up Project/april_con.csv")

april_org<-data %>%
  tbl_df() %>%
  select(Date, AveragePrice, Total.Volume, type, region) %>%
  filter(data$Date >= as.Date("2015-04-01") & data$Date < as.Date("2015-05-01") & type == "organic")

april_org<-april_org%>%
  select(AveragePrice, Total.Volume, region) %>%
  group_by(region)%>%
  summarise_all(funs(mean))

april_org$Total.Volume<-april_org$Total.Volume*30

april_org$Date="2015-04"
april_org$type="organic"

write.csv(april_org, "C:/Users/skenn/Desktop/UVM/CS 205/Warm-Up Project/april_org.csv")

##########################################################
march_con<-data %>%
  tbl_df() %>%
  select(Date, AveragePrice, Total.Volume, type, region) %>%
  filter(data$Date >= as.Date("2015-03-01") & data$Date < as.Date("2015-04-01") & type == "conventional")

march_con<-march_con%>%
  select(AveragePrice, Total.Volume, region) %>%
  group_by(region)%>%
  summarise_all(funs(mean))

march_con$Total.Volume<-march_con$Total.Volume*31

march_con$Date="2015-03"
march_con$type="conventional"

write.csv(march_con, "C:/Users/skenn/Desktop/UVM/CS 205/Warm-Up Project/march_con.csv")

march_org<-data %>%
  tbl_df() %>%
  select(Date, AveragePrice, Total.Volume, type, region) %>%
  filter(data$Date >= as.Date("2015-03-01") & data$Date < as.Date("2015-04-01") & type == "organic")

march_org<-march_org%>%
  select(AveragePrice, Total.Volume, region) %>%
  group_by(region)%>%
  summarise_all(funs(mean))

march_org$Total.Volume<-march_org$Total.Volume*31

march_org$Date="2015-03"
march_org$type="organic"

write.csv(march_org, "C:/Users/skenn/Desktop/UVM/CS 205/Warm-Up Project/march_org.csv")

##########################################################
february_con<-data %>%
  tbl_df() %>%
  select(Date, AveragePrice, Total.Volume, type, region) %>%
  filter(data$Date >= as.Date("2015-02-01") & data$Date < as.Date("2015-03-01") & type == "conventional")

february_con<-february_con%>%
  select(AveragePrice, Total.Volume, region) %>%
  group_by(region)%>%
  summarise_all(funs(mean))

february_con$Total.Volume<-february_con$Total.Volume*28

february_con$Date="2015-02"
february_con$type="conventional"

write.csv(february_con, "C:/Users/skenn/Desktop/UVM/CS 205/Warm-Up Project/february_con.csv")

february_org<-data %>%
  tbl_df() %>%
  select(Date, AveragePrice, Total.Volume, type, region) %>%
  filter(data$Date >= as.Date("2015-02-01") & data$Date < as.Date("2015-03-01") & type == "organic")

february_org<-february_org%>%
  select(AveragePrice, Total.Volume, region) %>%
  group_by(region)%>%
  summarise_all(funs(mean))

february_org$Total.Volume<-february_org$Total.Volume*28

february_org$Date="2015-02"
february_org$type="organic"

write.csv(february_org, "C:/Users/skenn/Desktop/UVM/CS 205/Warm-Up Project/february_org.csv")

##########################################################
january_con<-data %>%
  tbl_df() %>%
  select(Date, AveragePrice, Total.Volume, type, region) %>%
  filter(data$Date >= as.Date("2015-01-01") & data$Date < as.Date("2015-02-01") & type == "conventional")

january_con<-january_con%>%
  select(AveragePrice, Total.Volume, region) %>%
  group_by(region)%>%
  summarise_all(funs(mean))

january_con$Total.Volume<-january_con$Total.Volume*31

january_con$Date="2015-01"
january_con$type="conventional"

write.csv(january_con, "C:/Users/skenn/Desktop/UVM/CS 205/Warm-Up Project/january_con.csv")

january_org<-data %>%
  tbl_df() %>%
  select(Date, AveragePrice, Total.Volume, type, region) %>%
  filter(data$Date >= as.Date("2015-01-01") & data$Date < as.Date("2015-02-01") & type == "organic")

january_org<-january_org%>%
  select(AveragePrice, Total.Volume, region) %>%
  group_by(region)%>%
  summarise_all(funs(mean))

january_org$Total.Volume<-january_org$Total.Volume*31

january_org$Date="2015-01"
january_org$type="organic"

write.csv(january_org, "C:/Users/skenn/Desktop/UVM/CS 205/Warm-Up Project/january_org.csv")
