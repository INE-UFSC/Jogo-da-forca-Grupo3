import os

#FUNCAO ESPERA UM INTEIRO DE 0 A 5
def Renderizar_Boneco(vidas):
    os.system("clear")
    imagem = "forca_"+str(vidas)+".txt"
    with open(imagem,"r") as boneco:
        boneco = boneco.read()
        print(boneco)


vidas = int(input("Numero de vidas: "))
Renderizar_Boneco(vidas)
