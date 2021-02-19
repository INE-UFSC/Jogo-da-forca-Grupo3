import os

def Iniciar(): #Bernardo
    erro = True
    palavra = ""
    acertos = []
    while erro:
        erro = False
        palavra = input("   Palavra(s) a adivinhar: ")
        palavra = palavra.upper()
        acertos = list()
        for i in range(len(palavra)):
            acertos.append("_")
            if palavra[i] not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ ":
                erro = True
        if erro:
            print("   Caracteres inválidos na(s) palavra(s), insira novamente.")
            print("   Dica: evite acentos, números, pontuação, e 'ç'")
        else: acertos.append(' ')
    for i in range(25):
        print()
    return [palavra,acertos]

def Ler_Letra(palavra, letra, erros, acertos):  # VIcTOR
# ESSA FUNCAO LE UMA UNICA LETRA, CONFERE SE ELA EH VALIDA E VE SE EXISTE NA PALAVRA
# Letras repetidas e não repetidas acertadas => correta = True
# Letras repetidas e não repetidas ERRADAS => correta = False
    correta = False
    letra = letra.upper()
    while len(letra) != 1 or letra not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        letra = input("   Letra invalida, insira novamente: ")
        letra = letra.upper()

    for cada_letra in acertos:
        if cada_letra == letra:
            correta = True
            break
    for cada_letra in palavra:
        if cada_letra == letra:
            correta = True
            break
    return [correta,letra]

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
    if vidas>0:
        print(f"Você ainda tem {vidas} chances!")

    return[erros,acertos,vidas]

def Renderizar_Boneco(vidas): #Bernardo
    for i in range(25):
        print()
    # os.system("clear") Limpa no terminal (Tava ruim no pycharm dai tiramo)
    imagem = "forca_"+str(vidas)+".txt"
    with open(imagem,"r") as boneco:
        boneco = boneco.read()
        for i in range(4):
            print()
        print(boneco)

# A PARTIR DAQUI N EH FUNCAO (Otavio)

print("   Bem vindo ao jogo da forca, um jogo estranhamente mórbido para se")
print("   ensinar vocabulário a crianças do 3º ano do fundamental! ")
print()

while True: # LOOP, CONTINUA O JOGO ATE O JOGADOR SAIR
    palavra, acertos = Iniciar()
    erros = []
    vida = 5
    erros, acertos, vida = Escreve_Palavra(palavra,' ',True,erros,acertos,vida)
    while True: #LOOP LOGICO, PARAR ASSIM QUE GANHAR OU PERDER
        
        print()
        letra = input("   Adivinhe uma letra: ")
        correta , letra = Ler_Letra(palavra, letra, erros, acertos)
        erros, acertos, vida = Escreve_Palavra(palavra,letra,correta,erros,acertos,vida)
        
        if '_' not in acertos: # CHECAR VITORIA
            print(f'\n             ', end=" ")
            print(f"Você Venceu!")
            break
        
        elif vida == 0: #CHECAR DERROTA
            print(f'\n             ', end=" ")
            print(f"Você Perdeu...")
            print(f'\n             ', end=" ")
            print(f"A palavra era {palavra}.")
            break
    
    print(f'\n             ', end=" ")
    revanche = input(f"Gostaria de jogar novamente? Sim ou Não? ").upper()
    if revanche not in ['S','SIM','Y','YES']:
        break
input("https://www.youtube.com/watch?v=le5uGqHKll8    ")