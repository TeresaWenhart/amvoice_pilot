#estimate response bias per participant and task


datalist<-ls(pattern="Instrument_Pilot_experiment_P[0-9]{2}_[A-Z]{2}")
mylist<-list()
for (i in 1:length(datalist)){
  thisdata<-get(datalist[[i]])
  Hits<-sum(thisdata$key_num)/length(thisdata$key_num)
  Hits[Hits==1]<-0.9999
  Hits[Hits==0]<-0.0001
  
  
  ???????????????????????? #response bias possible for 
    #ambiguous stimuli? What is a Hit, what is a false alarm? 
  FA<-(AEFTresults[,15]-AEFTresults[,13])/AEFTresults[,15]
  FA[FA==1]<-0.9999
  FA[FA==0]<-0.0001
  d0=qnorm(Hits)-qnorm(FA)
  c0=-0.5*(qnorm(Hits)+qnorm(FA))
  rm(Hits,FA)
