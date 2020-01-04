import os
import string

parte1 = "wget https://www.fimi.com/media/Productattachments//f/i/fimi-a3-rc-"
parte2 = ".zip -P remotecontrol_fw/"

letras = list(string.ascii_lowercase)

numeros = range(1000,1025,1)

versoesRC = ["","_1","_2","_3"]

for letra in letras :
    for numero in numeros :
        for versaoRC in versoesRC :
            comando = parte1 + str(numero)+ "-" + letra + versaoRC + parte2
            print("--------------------------")
            print("BAIXANDO: " + comando)
            os.system(comando)
            print("--------------------------")