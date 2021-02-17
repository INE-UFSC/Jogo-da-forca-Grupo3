import os

def Iniciar(): #Bernardo
    palavra = input("Palavra a ser acertada: ")
    os.system("clear")
    return palavra

def Ler_Letra(palavra,letra,erros,acertos): #VITOR
    #ESSA FUNCAO LE UMA UNICA LETRA, CONFERE SE ELA EH VALIDA E VE SE EXISTE NA PALAVRA
    return [acertou]

def Escreve_Palavra(palavra,letra,correta,erros,acertos,vidas): #ARTHUR
    #ATRIBUI A LETRA NOS ACERTOS OU ERROS
    #AQUI ELA ESCREVE AS COISA NA TELA
    letra = letra.upper()
    palavra = palavra.upper()
    if correta == True:
        for i in range(len(palavra)):
            if palavra[i] == letra:
                acertos[i] = letra
    else:
        erros.append(letra)
        vidas = vidas-1
        
    Renderizar_Boneco(vidas)
    print()
    print(f'                ', end=" ")
    for l in acertos:
        print(f"{l}", end=" ")
    
    print()
    print(f'\n             ', end=" ")
    print("ERROS: ",end=" ")
    for e in erros:
        print(f"{e}", end=" ")
    
    print()
    print(f'\n             ', end=" ")
    print(f"Você ainda tem {vidas} chances!")

    return[erros,acertos]

#Pessoa casa tudo (Otavio)

#FUNCAO ESPERA UM INTEIRO DE 0 A 5
def Renderizar_Boneco(vidas): #Bernardo
    os.system("clear")
    imagem = "forca_"+str(vidas)+".txt"
    with open(imagem,"r") as boneco:
        boneco = boneco.read()
        print(boneco)

# A PARTIR DAQUI N EH FUNCAO

# VE SE FUNCIONOU AI KKKK

#ve se foi --Victor

palavra = "palavra"
erros = []
acertos = [] #lista com os caracteres
vidas = 5
Renderizar_Boneco(vidas)
