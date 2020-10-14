%create conditions file for auditory experiment

%folder of stimuli
cd C:\Users\teresa\Documents\UZH_Arbeit\Human_instrument_morphing\Experiment_trials\Timbre_task
filedir='C:\Users\teresa\Documents\UZH_Arbeit\Human_instrument_morphing\Experiment_trials\Timbre_task\'
condition_dir='..\Experiment_trials\Timbre_task\'
filelist=dir('*.wav')


trialnr=[1:1:4*72]'
trial=[1:1:72]'
morphrate1=cell(72,1)
morphrate2=cell(72,1)
Block=cell(72,1)
Category1=cell(72,1)
Category2=cell(72,1)
Prototype1=cell(72,1)
Prototype2=cell(72,1)
names=cell(72,1)
directory=cell(72,1)


for i=1:72
    filename=filelist(i,1).name
    names{i,:}=[condition_dir,filename]
    Block{i,:}="Tim"
    Stimulus=filename(1:17)
    Category1{i,:} = Stimulus(1:3)
    Prototype1{i,:} = Stimulus(4)
    Category2{i,:} = Stimulus(6:8)
    Prototype2{i,:} = Stimulus(9)
    morphrate1{i,:}= Stimulus(11:13)
    morphrate2{i,:}= Stimulus(15:17)
end


mytable=table(trial, Block, Category1, Prototype1, Category2, Prototype2, morphrate1, morphrate2, names)

mytable=repmat(mytable,[4 1])

%--------------------
%try to find a random order, where neighboring rows do not have the same
%instruments/voices
%--------------------

%initial new order
randtrials= randperm(288)
newtable=mytable(randtrials,:)

%find inidces of rows i, that contain the same sounds as the row i-1

while (i~=288) | (indices~=0)
    indices=[]
    for i=2:287
                A=char(table2cell(newtable(i,3)))
                B=char(table2cell(newtable(i-1,3)))
                E=char(table2cell(newtable(i,4)))
                F=char(table2cell(newtable(i-1,4)))
                if (A==B) & (E==F)
                    indices=[indices,i]
                    i=i+1
                else
                    i=i+1
                end
    end

    %----remove wrong rows from table
    T1=newtable
    T1(indices,:)=[]
    T2=newtable(indices,:)
    %----concatenate tables again
    newtable=[T1;T2]
    %---repeat loop as often as necessary, to find random order
end 




mytable = addvars(mytable,trialnr,'Before','trial');
writetable(mytable,'conditions_Timbre.csv', 'Delimiter',',')

newtable = addvars(newtable,trialnr,'Before','trial');
writetable(newtable,'conditions_Timbre_rand.csv', 'Delimiter',',') 

clear
clc
