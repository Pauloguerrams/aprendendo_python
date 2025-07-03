resposta = input()
print ("O programa funciona?")
if(resposta=='SIM'):
    resposta= input()
    print("Você entende o que fez?")
    if(resposta == 'SIM'):
        print("Ótimo. Então não mexe!")
    else:  
        resposta = input()
        print("Já foi na tutoria?")
        if(resposta == 'SIM'):
            print("Choremos!")
        else:
            print("Temos um time a disposição!") 
else:
    resposta = input()
    print("Você sabe onde está o erro?")   
    if(resposta == 'SIM'):
        resposta = input() 
        print("Acha que pode solucionar sozinho?")
        if(resposta == 'SIM'):
            print("Então mão na massa!")
        else:
            resposta = input()
            print("Já pesquisou no Google?")
        if(resposta == 'NÃO'):
            print("Corre lá então!")    
        else:
            resposta = input()
            print("Já foi na tutoria?")
            if(resposta == 'SIM'):
                print("Choremos!")
            else:
                print("Temos um time a disposição!")
    else:  
        resposta = input()
        print("Já foi na tutoria?")
        if(resposta == 'SIM'):
            print("Choremos!")
        else:
            print("Temos um time a disposição!") 