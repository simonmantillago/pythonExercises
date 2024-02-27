import os
def main():
    os.system('clear')
    num1 = obtener_numero("Ingrese el primer número entero positivo: ")
    num2 = obtener_numero("Ingrese el segundo número entero positivo: ")
    num3 = obtener_numero("Ingrese el tercer número entero positivo: ")

    suma = num1 + num2 + num3

    print("La sumatoria de los tres números es:", suma)

def obtener_numero(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            if numero < 0:
                print("Error: Debe ingresar un número entero positivo.")
                os.system('clear')
            else:
                return numero
        except ValueError:
            print("Error: Debe ingresar un número entero.")



if __name__ == "__main__":
    main()
