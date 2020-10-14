#prepare analysis averaging over participants

library(tidyr)
library(dplyr)
library(purrr)
library(ggplot2)

#first, create tables for conditions and subjects with preprocessing

#rbind all participants tables
datalist<-ls(pattern="Pilot_experiment_P[0-9]{2}_[A-Z]{2}")
mylist<-list()
for (i in 1:length(datalist)){
  thisdata<-get(datalist[[i]])
  thisdata$morphrate1<-as.numeric(as.character(thisdata$morphrate1))
  thisdata$morphrate2<-as.numeric(as.character(thisdata$morphrate2))
  thisdata$Block<-as.factor(thisdata$B)
  thisdata$Category1<-as.factor(thisdata$Category1)
  thisdata$Category2<-as.factor(thisdata$Category2)
  mylist[[i]]<-thisdata
}
allsubjects<-dplyr::bind_rows(mylist)
allsubjects$morphrate1<-as.numeric(as.character(allsubjects$morphrate1))
allsubjects$morphrate2<-as.numeric(as.character(allsubjects$morphrate2))
allsubjects$Block<-as.factor(allsubjects$Block)



############################
#fit and plot psychometric function
############################
library(quickpsy)
library(DEoptim)
library(parallel)


allsubjects <- na.omit(allsubjects) 
fit <- quickpsy(d=allsubjects, x=morphrate12, k=key_num, grouping = .(Block), B = 10)
pcurve<-plotcurves(fit)
pcurve+scale_x_continuous(limits=c(0.0,1))+ggtitle("all subjects")
parplot<-plotpar(fit)
parplot+scale_y_continuous(limits=c(0.0,1))+ggtitle("all subjects")
thresplot<-plotthresholds(fit, geom = 'point')
thresplot+scale_y_continuous(limits=c(0.0,1))+ggtitle("all subjects")


###########################
#fit and plot psychometric function per subject
###########################
for (i in 1:length(mylist)){
  thisdata<-mylist[i]
  thisdata<-as.data.frame(thisdata)
  name<-datalist[[i]]
  thisdata <- na.omit(thisdata) 
  fit <- quickpsy(d=thisdata, x=morphrate2, k=ans_num, grouping = .(Block), B = 10)
  pcurve<-plotcurves(fit)
  pcurve<-pcurve+scale_x_continuous(limits=c(0.0,1))+ggtitle(name)+ggtitle(name)
  print(pcurve)
  parplot<-plotpar(fit)
  parplot<-parplot+scale_y_continuous(limits=c(0.0,1))+ggtitle(name)
  print(parplot)
  thresplot<-plotthresholds(fit, geom = 'point')
  thresplot<-thresplot+scale_y_continuous(limits=c(0.0,1))+ggtitle(name)
  print(thresplot)
}
