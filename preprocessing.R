#preprocessing morphing experiment (prestudy)

#library
library(dplyr)
library(tidyr)
#directory
setwd("~/UZH_Arbeit/Human_instrument_morphing/PsychoPy/data")

path<-paste(getwd())


#read version A files

sub.folders <- list.files(path=getwd(), pattern="A_P[0-9]{2}_[A-Z]{2}_[0-9]{4}_[A-Za-z]{3}_[0-9]{2}_[0-9]{4}",include.dirs = TRUE)
for (j in sub.folders) {
  path<-paste(getwd(),"/",j,sep="")
  filenames = list.files(path=path,pattern="Pilot_experiment_P[0-9]{2}_[A-Z]{2}.csv")
  for (i in filenames) {
    name <- gsub(".csv","",i)
    name<-paste("A_",name, sep="")
    name <-gsub("/","_",name)
    assign(name,read.csv(paste(path,"/",i,sep=""))) #read in the table and name as "name"
  }
}


#create separate and sparse tables for each Set of Stimuli per Subject
file_list<-ls(pattern="A_Pilot_experiment_P[0-9]{2}_[A-Z]{2}")
for (i in 1:length(file_list)) {
  name=file_list[i]
  name=gsub("A_","",name)
  thistable<-get(file_list[i])
  thistable$key_num<-dplyr::recode(thistable$key, "right" = 1, "left" = 0)
  Gender<-dplyr::filter(thistable,thistable$Block=="Gen")
  Instrument<-dplyr::filter(thistable,thistable$Block=="Ins")
  Voice<-dplyr::filter(thistable,thistable$Block=="Voc")
  Timbre<-dplyr::filter(thistable,thistable$Block=="Tim")
  ####################
  assign(name,thistable)
  name2<-paste("Gender_",name, sep="")
  assign(name2,Gender)
  name3<-paste("Instrument_",name, sep="")
  assign(name3,Voice)
  name4<-paste("Voice_",name, sep="")
  assign(name4,Instrument)
  name5<-paste("Timbre_",name, sep="")
  assign(name5,Timbre)
  i=i+1
}


#read version B files

sub.folders <- list.files(path=getwd(), pattern="B_P[0-9]{2}_[A-Z]{2}_[0-9]{4}_[A-Za-z]{3}_[0-9]{2}_[0-9]{4}",include.dirs = TRUE)
for (j in sub.folders) {
  path<-paste(getwd(),"/",j,sep="")
  filenames = list.files(path=path,pattern="Pilot_experiment_P[0-9]{2}_[A-Z]{2}.csv")
  for (i in filenames) {
    name <- gsub(".csv","",i)
    name<-paste("B_",name, sep="")
    name <-gsub("/","_",name)
    assign(name,read.csv(paste(path,"/",i,sep=""))) #read in the table and name as "name"
  }
}

#create separate and sparse tables for each Set of Stimuli per Subject
file_list<-ls(pattern="B_Pilot_experiment_P[0-9]{2}_[A-Z]{2}")
for (i in 1:length(file_list)) {
  name=file_list[i]
  name=gsub("B_","",name)
  thistable<-get(file_list[i])
  thistable$key_num<-dplyr::recode(thistable$key, "right" = 0, "left" = 1)
  Gender<-dplyr::filter(thistable,thistable$Block=="Gen")
  Instrument<-dplyr::filter(thistable,thistable$Block=="Ins")
  Voice<-dplyr::filter(thistable,thistable$Block=="Voc")
  Timbre<-dplyr::filter(thistable,thistable$Block=="Tim")
  ####################
  assign(name,thistable)
  name2<-paste("Gender_",name, sep="")
  assign(name2,Gender)
  name3<-paste("Instrument_",name, sep="")
  assign(name3,Voice)
  name4<-paste("Voice_",name, sep="")
  assign(name4,Instrument)
  name5<-paste("Timbre_",name, sep="")
  assign(name5,Timbre)
  i=i+1
}



