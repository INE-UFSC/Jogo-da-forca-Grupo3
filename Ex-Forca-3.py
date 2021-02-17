import os

def Iniciar(): #Bernardo
    palavra = input("Palavra a ser acertada: ")
    os.system("clear")
    return palavra

def Ler_Letra(palavra,letra,erros,acertos): #VITOR
    #ESSA FUNCAO LE UMA UNICA LETRA, CONFERE SE ELA EH VALIDA E VE SE EXISTE NA PALAVRA
    return [acertou]

def Escreve_Palavra(palavra,letra,correta): #ARTHUR
    #ATRIBUI A LETRA NOS ACERTOS OU ERROS
    #AQUI ELA ESCREVE AS COISA NA TELA
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

palavra = "palavra"
erros = []
acertos = [] #lista com os caracteres
vidas = int(input("Numero de vidas: "))
Renderizar_Boneco(vidas)
