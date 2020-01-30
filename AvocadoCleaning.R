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

write.csv(august_con, "C:/Users/skenn/Desktop/UVM/CS 205/Warm-Up Project/august_con.csv")

august_org<-data %>%
  tbl_df() %>%
  select(Date, AveragePrice, Total.Volume, type, region) %>%
  filter(data$Date >= as.Date("2015-08-01") & data$Date < as.Date("2015-09-01") & type == "organic")

august_org<-august_org%>%
  select(AveragePrice, Total.Volume, region) %>%
  group_by(region)%>%
  summarise_all(funs(mean))

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

january_org$Date="2015-01"
january_org$type="organic"

write.csv(january_org, "C:/Users/skenn/Desktop/UVM/CS 205/Warm-Up Project/january_org.csv")
