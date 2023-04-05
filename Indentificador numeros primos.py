def run():
    numero=abs(int(input("Ingrese por favor el numero que quieres verificar si es primo: ")))

    def mensaje(clasificator):
        print("el " + str(numero) +" "+ clasificator + " es un numero primo")

    def es_primo():
        for n in (range(2, numero)):
            if numero % n == 0 or (numero ==1 and numero==0):
                return False
            else:
                return True

    if es_primo():
        mensaje("SI")
    else:
        mensaje("NO")

if __name__ == '__main__':
        run()

