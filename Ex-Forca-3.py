import os

def Iniciar(): #Bernardo
    erro = True
    palavra = ""
    acertos = []
    while erro:
        erro = False
        palavra = input("Palavra a ser acertada: ")
        palavra = palavra.upper()
        acertos = list()
        for i in range(len(palavra)):
            acertos.append("_")
            if palavra[i] not in "ABCDEFGHIJKLMNOPQRSTUVXZ":
                erro = True
        if erro: print("Caracteres invalidos na palavra, insira novamente")
    return [palavra,acertos]

def Ler_Letra(palavra, letra, erros, acertos):  # VIcTOR
# ESSA FUNCAO LE UMA UNICA LETRA, CONFERE SE ELA EH VALIDA E VE SE EXISTE NA PALAVRA
# Letras repetidas e não repetidas acertadas => correta = True
# Letras repetidas e não repetidas ERRADAS => correta = False
    correta = False
    letra = letra.upper()
    if len(letra) == 1 and letra in "ABCDEFGHIJKLMNOPQRSTUVXZ":
        for cada_letra1 in acertos:
            if cada_letra1 != letra:
                correta = False
            else:
                correta = True
                break
        for cada_letra2 in palavra:
            if cada_letra2 != letra:
                correta = False

            else:
                correta = True
                break
    else:
        print("Essa letra nao eh valida")
    return correta

def Escreve_Palavra(palavra,letra,correta,erros,acertos,vidas): #ARTHUR
    #ATRIBUI A LETRA NOS ACERTOS OU ERROS E IMPRIME O JOGO NA TELA
    letra = letra.upper()
    if correta:
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

def Renderizar_Boneco(vidas): #Bernardo
    #os.system("clear")
    imagem = "forca_"+str(vidas)+".txt"
    with open(imagem,"r") as boneco:
        boneco = boneco.read()
        print(boneco)

# A PARTIR DAQUI N EH FUNCAO

palavra, acertos = Iniciar()
letra = input("Letra: ")
erros = []
vida = 0
correta = Ler_Letra(palavra, letra, erros, acertos)
erros, acertos = Escreve_Palavra(palavra,letra,correta,erros,acertos,vida)
