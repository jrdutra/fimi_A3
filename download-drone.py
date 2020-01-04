import os
import string

parte1 = "wget https://www.fimi.com/media/Productattachments//f/i/fimi-a3-fc-"
parte2 = ".zip -P drone_fw/"

letras = list(string.ascii_lowercase)

numeros = range(950,1050,1)

for letra in letras :
    for numero in numeros :
        comando = parte1 + str(numero) + "-" + letra + parte2
        print("--------------------------")
        print("BAIXANDO: " + parte1 + str(numero) + "-" + letra + parte2)
        os.system(comando)
        print("--------------------------")