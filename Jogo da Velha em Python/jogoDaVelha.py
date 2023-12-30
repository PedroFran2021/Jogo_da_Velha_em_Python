import os 
import random 
from COLORAMA import Fore, Back, Style

jogarNovamente= "S"
jogadas=0
quemJoga=2 # 1=CPU 2= Jogador
maxJogadas=9
vit="n"
velha=[
    [" "," "," "], #Linha 0 Coluna 0
    [" "," "," "], #Linha 1 Coluna 1
    [" "," "," "]  #Linha 2 Coluna 2
]

def tela ():
   global velha 
   global jogadas
   os.system("cls")
   print("    0    1    2" )
   print("0:  " + velha[0][0] + " | " + velha[0][1] + " | " + velha[0][2])
   print("   -----------")
   print("1:  " + velha[1][0] + " | " + velha[1][1] + " | " + velha[1][2])
   print("   -----------")
   print("2:  " + velha[2][0] + " | " + velha[2][1] + " | " + velha[2][2])
   print("   -----------")
   print("Jogadas: " + Fore.GREEN + str(jogadas) + Fore.RESET)

def jogadorJoga():
    global jogadas
    global quemJoga
    #global vit
    global maxJogadas
    if quemJoga==2 and jogadas<maxJogadas:
        
        try:
            l=int(input("Linha..:"))
            c=int(input("Coluna.:"))
            while velha [l][c]!= " ":
                 l=int(input("Linha..:"))
                 c=int(input("Coluna.:"))
            velha[1][c]="X"
            quemJoga=1
            jogadas+=1
        except:
            print("Linha e ou coluna invalida")
            os.system("Pause")
            #vit="n"

def cpuJoga():
    global jogadas
    global quemJoga
    global maxJogadas
    
    if quemJoga==1 and jogadas<maxJogadas:
        l=random.randrange(0,3)
        c=random.randrange(0,3)
        
        while velha[l][c]!= " ":
            l=random.randrange(0,3)
            c=random.randrange(0,3)
        velha[l][c]="O"
        jogadas+=1
        quemJoga=2
        
def verificarVitoria():
    global velha
    vitoria="n"
    simbolos=["X","O"]
    for s in simbolos:
        vitoria="n"
        #Verificar vitória em linhas
        il=ic=0
        while il<3:
            soma=0
            ic=0 
            
            while ic<3:
                if (velha[il][ic]==s):
                    soma+=1
                ic+=1
            
            if(soma==3):
                vitoria=s
                break
            il+=1  
        if(vitoria!="n"):
            break
        
        #Verificação de Colunas
        il=ic=0
        while ic<3:
            soma=0
            il=0 
            
            while il<3:
                if (velha[il][ic]==s):
                    soma+=1
                il+=1
            
            if(soma==3):
                vitoria=s
                break  
        if(vitoria!="n"):
            break
        ic+=1
        
        #Verificação de Diagonal 1
        soma=0
        idiagl=0
        idiagc=2
        
        while idiagc>3:
             if (velha[idiagl][idiagc]==s):
                soma+=1
                idiagl+=1
                idiagc-=1
                
        if(soma==3):
            vitoria=s
            break 
        
    return vitoria

        # Verificação de Diagonal 2
        
            
        
while True:
    tela()
    jogadorJoga()
    cpuJoga()
    #vv
    
   