from probability import BayesNet, DecisionNetwork, enumeration_ask ,InformationGatheringAgent,elimination_ask


T = bool(True)
F = bool(False)

class DecisionNetworkHealth(DecisionNetwork):
   def __init__(self):
      
        Actions = ('Action', [], ['TakeAspirin' ,"NoTakeAspirin"])
        super().__init__(Actions, enumeration_ask)
        
        for node in self.inicializarRede():
            super().add(node)
        
   def inicializarRede(self):
      
         Flu = ('Flu', [], 0.05)

         Fever = ('Fever', ['Flu'], {T: 0.95, F: 0.02})

         Therm = ('Therm', ['Fever'], {T: 0.90, F: 0.05})

         FeverLater = ('FeverLater', ['Fever', 'TakeAspirin'], {
            (T, T): 0.05,
            (T, F): 0.90,
            (F, T): 0.01,
            (F, F): 0.02,
         })

         Reaction = ('Reaction', 'TakeAspirin', {(T,): 0.05, (F,): 0.00})


         #action

         TakeAspirin = ('TakeAspirin', ['Therm'], {(True):0.1 ,(False): 0.1})
   
         # rede 
         nodes =[Flu,Fever,Therm,TakeAspirin,FeverLater,Reaction]
         
         return nodes

    
   def get_utility(self, action, state):
      if(action  and state):
         return -50
      elif(action):
         return -10
      elif(state):
         return -30
      else:
         return 50
         
    
   def best_action(self,evidence):
        
        bestAction = ('', float('-inf'))
        
        
        list = [True,False]
        for action in list:
         evidence1 ={'TakeAspirin':action}
         evidence1.update(evidence)
         
         u =0.0
         if('Reaction' not in evidence):
            try:
               probR = self.infer('Reaction', evidence1, self).prob   
            except:
               probR ={True:0 ,False:0} 
         
         try:
            probF = self.infer('FeverLater', evidence1, self).prob
         except:
            probF ={True:0 ,False:0} 
         
         for itemF in probF:
            if('Reaction' not in evidence):
               for itemR in probR: 
                  u += probR[itemR] *probF[itemF] * self.get_utility(itemF,itemR)
           
            else:
               u += probF[itemF] * self.get_utility(itemF,evidence['Reaction'])
               
         print(action,u)
         
         if(u > bestAction[1]):
            bestAction = (action,u)

        return 'TakeAspirin' if bestAction[0] else 'NoTakeAspirin'
  
   def getEvidencia(self):
      evidence = {}

      lista =input("Digite as evidencias\n")

      if(lista.count != 0):
         for dado in lista.split(','):
            valor = dado.split(':')
            evidence[str(valor[0])] = True if valor[1].lower() == "true" else False
            
      return evidence
   
  

redeModestia = DecisionNetworkHealth()



   
print(redeModestia.best_action(redeModestia.getEvidencia()))

