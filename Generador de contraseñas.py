import random
def creater_contrasena(l):
    nueva_contrasena = []
    mayus = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T',
             'U', 'V', 'X', 'Y', 'Z']
    minus = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't',
             'u', 'v', 'x', 'y', 'z']
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    caract = ['*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°',
              '^', '&', '$', '#', '"']
    suma_caracteres = mayus + minus + nums + caract
    for i in range(0,l):
        caracter_random= random.choice(suma_caracteres)
        nueva_contrasena.append(caracter_random)
    nueva_contrasena="".join(nueva_contrasena)
    return nueva_contrasena


def run():
    numero_caracteres=int(input("Por favor ingrese el numero de parametros que necesita su contraseña: "))
    nueva_contrasena=creater_contrasena(numero_caracteres)
    print("tu nueva contrasena generada  es la siguiente: "+nueva_contrasena)

if __name__ == '__main__':
    run()
