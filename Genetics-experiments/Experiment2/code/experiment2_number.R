library(ggplot2)
library(dplyr)
library(ggsci)

library(introdataviz)
library(pacman)

raw_data <- read.csv('../03_Data/clean_R.csv',header=TRUE, sep=",")

class1_data <- raw_data[which(raw_data$class == 1),]
class1_clean_data <- dplyr::filter(class1_data, !is.na(sex))

p <- ggplot(class1_clean_data, aes(factor(type,levels = c("ABC","abc","AbC","aBc","aBC","Abc","ABc","abC")), number,fill=sex))
p+geom_bar(stat="identity",position="dodge")+
  theme_classic(base_line_size = 1)+
  labs(x="F2",y="Number",family="Times",size=10)+
  theme(axis.text.x = element_text(size = 12),axis.text.y  = element_text(size = 12),plot.title = element_text(hjust = 0.5))+
  ggtitle("The number of F2")+
  scale_color_npg()+
  scale_fill_npg()

p2 <- ggplot(raw_data, aes(factor(type,levels = c("ABC","abc","AbC","aBc","aBC","Abc","ABc","abC")), number,fill = type))

p2 + geom_col()+
  theme_classic(base_line_size = 1)+
  labs(x="F2",y="Number",family="Times",size=10)+
  theme(axis.text.x = element_text(size = 12),axis.text.y  = element_text(size = 12),plot.title = element_text(hjust = 0.5))+
  ggtitle("The number of F2")+
  scale_color_npg()+
  scale_fill_npg()

sum(raw_data[which(raw_data$type=="ABC"),]$number)
sum(raw_data[which(raw_data$type=="abc"),]$number)
sum(raw_data[which(raw_data$type=="AbC"),]$number)
sum(raw_data[which(raw_data$type=="aBc"),]$number)
sum(raw_data[which(raw_data$type=="aBC"),]$number)
sum(raw_data[which(raw_data$type=="Abc"),]$number)
sum(raw_data[which(raw_data$type=="ABc"),]$number)
sum(raw_data[which(raw_data$type=="abC"),]$number)
