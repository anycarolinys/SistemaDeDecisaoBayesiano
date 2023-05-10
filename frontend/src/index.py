import js

import decision

rede =decision.DecisionNetworkHealth()
campoSaida = Element("respostaAspirina")

nosEvidencia = ["Fever","Therm","Reaction"]
evidencia ={}

def obter_valor():
    evidencia = {}
    valorFebre = js.document.querySelectorAll("#febre")
    valorTermometro = js.document.querySelectorAll("#termometro")
    valorReacao = js.document.querySelectorAll("#aspirina")
    
    for i in range(0,2):
        if(valorFebre[i].checked):
            evidencia[nosEvidencia[0]] = True if str(valorFebre[i].value) == "True" else False
        if(valorTermometro[i].checked):
            evidencia[nosEvidencia[1]] = True if str(valorTermometro[i].value) == "True" else False
        if(valorReacao[i].checked):
            evidencia[nosEvidencia[2]] = True if str(valorReacao[i].value) == "True" else False
    
    
    campoSaida.write(rede.best_action(evidencia))
    
    

