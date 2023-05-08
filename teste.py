from probability import BayesNet, DecisionNetwork, enumeration_ask ,InformationGatheringAgent,elimination_ask


T = bool(True)
F = bool(False)

class DecisionNetworkHealth(DecisionNetwork):
   def __init__(self, action, infer, Nodes):
        super().__init__(action, infer)
        
        for node in Nodes:
            super().add(node)
        
    
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
            probR = self.infer('Reaction', evidence1, self).prob
            
         probF = self.infer('FeverLater', evidence1, self).prob
         
         
         for itemF in probF:
            if('Reaction' not in evidence):
               for itemR in probR: 
                  u += probR[itemR] *probF[itemF] * self.get_utility(itemF,itemR)
           
            else:
               u += probF[itemF] * self.get_utility(itemF,evidence['Reaction'])
               
         
         
         if(u > bestAction[1]):
            bestAction = (action,u)

        return 'TakeAspirin' if bestAction[0] else 'NoTakeAspirin'
  
   def get_expected_utility(self, action, evidence):
        """Compute the expected utility given an action and evidence"""
        u = 0.0

        
        prob_dist = self.infer(action, evidence, self).prob
        for item, _ in prob_dist.items():
              u += prob_dist[item] * self.get_utility(action, item)

        return u



# Evidence 

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

# Decision
Actions = ('Action', [], ['TakeAspirin' ,"NoTakeAspirin"])

#utilidade
Utilidade = ('Utilidade', ['FeverLater', 'Reaction'], {})

# rede 
nodes =[Flu,Fever,Therm,TakeAspirin,FeverLater,Reaction]

redeModestia = DecisionNetworkHealth(Actions, enumeration_ask, nodes)


evidence = {}
action = 'FeverLater'

# print(redeModestia.get_expected_utility(action,evidence))
print(redeModestia.best_action(evidence))

# print(enumeration_ask(action,evidence,redeModestia).prob)

