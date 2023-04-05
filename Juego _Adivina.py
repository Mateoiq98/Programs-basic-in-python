import random

def run():
    numero_aleatorio=random.randint(3,3)
    numero_cliente=int(input("Hola este es el juego adivina el numero del 1 al 10! tienes 3 intentos, es decir 3 vidas, por favor trata de adivinar. intenta escribir  el numero: "))
    vidas=2
    while numero_cliente!=numero_aleatorio:
        while vidas >= 1:
            if numero_cliente<numero_aleatorio:
                print("busca un numero mayor, te quedan "+str(vidas)+" intentos o vidas" )
            else:
                print("busca un numero menor, te quedan "+str(vidas)+" intentos o vidas" )
            numero_cliente=int(input())
            vidas=vidas-1
        print("Lo siento te has quedado sin vidas o intentos, perdiste!")
        break
    if numero_cliente == numero_aleatorio:
        print("Has ganado felcitaciones!")

if __name__ == '__main__':
    run()