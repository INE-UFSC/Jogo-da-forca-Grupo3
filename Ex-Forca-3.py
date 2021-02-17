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

    return[erros,acertos,vidas]

def Renderizar_Boneco(vidas): #Bernardo
    #os.system("clear")
    imagem = "forca_"+str(vidas)+".txt"
    with open(imagem,"r") as boneco:
        boneco = boneco.read()
        print(boneco)

# A PARTIR DAQUI N EH FUNCAO

print("   Bem vindo ao jogo da forca, um jogo estranhamente mórbido para se")
print("   ensinar vocabulário a crianças do 3º ano do fundamental! ")
while True: # LOOP, CONTINUA O JOGO ATE O JOGADOR SAIR
    palavra, acertos = Iniciar()
    erros = []
    vida = 5
    while True: #LOOP LOGICO, PARAR ASSIM QUE GANHAR OU PERDER
        
        letra = input("Letra: ")
        for i in range(10):
            print()
        correta = Ler_Letra(palavra, letra, erros, acertos)
        erros, acertos, vida = Escreve_Palavra(palavra,letra,correta,erros,acertos,vida)
        
        if '_' not in acertos: # CHECAR VITORIA
            print(f'\n             ', end=" ")
            print(f"Você Venceu!")
            print(f'\n             ', end=" ")
            break
        
        elif vida == 0: #CHECAR DERROTA
            print(f'\n             ', end=" ")
            print(f"Você Perdeu...")
            print(f'\n             ', end=" ")
            print(f"A palavra era {palavra}.")
            print(f'\n             ', end=" ")
            break
        
    try:
        revanche = input(f"Gostaria de jogar novamente? (S)im ou (N)ão? ").upper()
        if revanche != 'S':
            break
    except:
        break
input("https://www.youtube.com/watch?v=le5uGqHKll8    ")