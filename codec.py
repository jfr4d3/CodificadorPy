print("1.Codificar")
print("2.Decodificar")
decision = int(input())
import string


def codificador():
    global mensaje
    mensaje_cod = ""
    for men in range(0, len(mensaje)):
        for alfa in range(0, len(alfabeto)):
            if mensaje[men] == alfabeto[alfa]:
                if alfa + nivel > len(alfabeto)-1:
                    new_ind = alfa + nivel - len(alfabeto)
                else:
                    new_ind = alfa + nivel
                alf_ind = alfabeto[new_ind]
                mensaje_cod = mensaje_cod + alf_ind

    print(mensaje_cod)


def decodificador():
    global mensaje
    mensaje_decod = ""
    for men in range(0, len(mensaje)):
        for alfa in range(0, len(alfabeto)):
            if mensaje[men] == alfabeto[alfa]:
                if alfa - nivel < 0:
                    new_ind = alfa - nivel +len(alfabeto)
                else:
                    new_ind = alfa - nivel

                alf_ind = alfabeto[new_ind]

                mensaje_decod = mensaje_decod + alf_ind

    print(mensaje_decod)


flag = True
while flag:
    if decision == 1:
        mensaje = input("Palabra a codificar: ")
        nivel = int(input("Nivel de codificacion: "))
        alfabeto = "qwertyuiopasdfghjklñzxcvbnm 1234567890"

        codificador()
        flag = False
    elif decision == 2:
        mensaje = input("Palabra a decodificar: ")
        nivel = int(input("Nivel de decodificacion: "))
        alfabeto = "qwertyuiopasdfghjklñzxcvbnm 1234567890"
        # alfabeto = "0987654321mnbvcxzñlkjhgfdsapoiuytrewq"
        decodificador()
        flag = False
    else:
        print("Introduce una opción valida")
