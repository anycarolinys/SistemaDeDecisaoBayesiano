from probability import BayesNet, DecisionNetwork, enumeration_ask ,InformationGatheringAgent

# Definir as constantes T e F para True e False, respectivamente
T = True
F = False

class DecisionNetworkHealth(DecisionNetwork):
   def __init__(self, action, infer, Nodes):
        super().__init__(action, infer)
        
        for node in Nodes:
            super().add(node)
        
    
   def get_utility(self, action, state):
     print(state)
     if action == "TakeAspirin" and state.get('Reaction1', False):
        return -50
     elif state.get('FeverLater', False) and state.get('Reaction', False):
        return -50
     elif state.get('FeverLater', False):
        return -10
     elif state.get('Reaction', False):
        return -30
     else:
        return 50
    
   def best_action(self,evidence):
        
        bestAction =('',0)
        
        for action in self.action[2]:
              score = self.get_expected_utility(action,evidence)
              if(score> bestAction[1]):
                    bestAction = (action,score)
               
        return bestAction[0]
  
   def get_expected_utility(self, action, evidence):
        """Compute the expected utility given an action and evidence"""
        u = 0.0
        # print(action,evidence)
        prob_dist = self.infer(action, evidence, self).prob
        print(prob_dist)
        for item, _ in prob_dist.items():
              print(item)
              u += prob_dist[item] * self.get_utility(action, item)

        return u


class AgentNetwork(InformationGatheringAgent):
    def __init__(self, decnet, infer, initial_evidence=None):
        super().__init__(decnet, infer, initial_evidence)
        
    def integrate_percept(self, percept):
        self.observation.append(percept)
        return self.observation

# Evidence 

Flu = ('Flu', [], 0.05)

Fever = ('Fever', ['Flu'], {T: 0.95, F: 0.02})

Therm = ('Therm', ['Fever'], {T: 0.95, F: 0.02})

FeverLater = ('FeverLater', ['Fever', 'TakeAspirin'], {
    (T, T): 0.05,
    (T, F): 0.90,
    (F, T): 0.01,
    (F, F): 0.02,
})
Reaction = ('Reaction', 'TakeAspirin', {T: 0.05, F: 0.0})


#action

TakeAspirin = ('TakeAspirin', ['Therm'], {})

# Decision
Actions = ('Action', [], ['TakeAspirin', 'DoNotTakeAspirin'])

#utilidade
Utilidade = ('Utilidade',['FeverLater','Reaction'], {})

# rede 
nodes =[Flu,Fever,Therm,TakeAspirin,FeverLater,Reaction]

redeModestia = DecisionNetworkHealth(Actions, enumeration_ask, nodes)
print(redeModestia)

evidence = {'Fever': True, 'Therm': True}
action = 'TakeAspirin'

AgenteRede = AgentNetwork (redeModestia,enumeration_ask,{})
# print(AgenteRede)

# print(AgenteRede.execute(evidence))