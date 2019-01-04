  import numpy as np 
  def pick_cutest(list_of_targets):
       """
       here you could put cutness metric as you like it's a persona flavour
       """
       return cutest
   def apply_strategy(strategy):
       """
       all you have to do here is doing as strategy says 
       ex:if strategy is showing interest or say flirting phrse do it 
       """
       return  got_accepted
   """
   this just for fun 
   a machine learning based software to help you crush on a girl 
   """
   list_of_strategies=[] # list  of best known crushing strategies
   list_of_targets=[] #list of all your target crushes 
   list_of_winning_strategies=[0]*len(list_of_strategies)
   got_accepted=false
   while not list_of_targets.empty():

       cute=pick_cutest[list_of_targets]
       list_of_targets.pop(cute)
       for strategy in list_of_strategies:
           got_accepted=apply_strategy(strategy)
           if got_accepted:
               list_of_winning_strategies[strategy]+=1

    models_deg=[1,2,3,4,5] #to test it on our data set using regression model
    models=[]
    for m in models_deg:
        model=np.polyfit(list_of_targets,list_of_winnig_strategies,m)
        models.append(model)
   """
   from here we have our model in models we can feed it with new targets not listed here and just apply 
   strategy=np.polyval(model,targets)
   and it will tell us the best strategy to use with this new target
     
     a side note: crushing like hacking you could  initiate attack on say 10 servers and you could find only one of them vulnerable to your attack 
     you still the winner cheer up !!!!
     """"""""
    

           
