import os
#FUNCAO ESPERA DE 0 A 5 LINHAS DE COGIDO
def Renderizar_Boneco(vidas):
    os.system("clear")
    imagem = "forca_"+str(vidas)+".txt"
    with open(imagem,"r") as boneco:
        boneco = boneco.read()
        print(boneco)


vidas = int(input("Numero de vidas: "))
Renderizar_Boneco(vidas)
