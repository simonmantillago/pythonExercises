import os
# 4. Se desea realizar un programa en Python que permita ingresar n números enteros positivos y cuando se
# Ingrese un numero negativo debe mostrar en pantalla el siguiente reporte.

# a. Total de números ingresados
# b. Total de números pares ingresados
# c. Promedio de los números pares
# d. Promedio de los números impares
# e. Cuantos números son menores que 10
# f. Cuantos números están entre 20 y 50
# g. Cuantos números son mayores que 100

def main():
    num_list = []
    print("""
          +++++++++++++++
          + Ejercicio 4 +
          +++++++++++++++
          """)
    
    num = obtener_numero('Ingrese un numero entero positivo para agregarlo a la lista o uno negativo para ver el menu de reportes \n ->', num_list)

    if num <= 0:
        menu_reportes(num_list)
        
        
        

def obtener_numero(mensaje,num_list):
    while True:
        try:
            numero = int(input(mensaje))
            if numero > 0: 
                os.system('cls')
            else:
                return numero
            add_num(numero,num_list)
            print('Numero agregado exitosamente')
            print(num_list)
            os.system('pause')
            os.system('cls')
        except ValueError:
            print("Error: Debe ingresar un número entero.")
        

def add_num(numero,num_list):
    num_list.append(numero)

def menu_reportes(num_list):
    while True:
        os.system('cls')
        print("""
    a. Total de números ingresados
    b. Total de números pares ingresados
    c. Promedio de los números pares
    d. Promedio de los números impares
    e. Cuantos números son menores que 10
    f. Cuantos números están entre 20 y 50
    g. Cuantos números son mayores que 100
    i. Volver
            """)
        opcion = input('->')

        if opcion == 'a':
            print('La cantidad de numeros ingresados es: ',len(num_list))
            os.system('pause')
            
        elif opcion == 'b':
            count = 0
            inCount = 0
            for idx,item in enumerate(num_list):
                if item % 2 == 0:
                    count +=1
                elif item % 2 != 0:
                    inCount += 1
            print('La cantidad de numeros pares ingresados es: ',count)
            os.system('pause')
        
        elif opcion == 'c':
            contador = 0
            nums = 0
            for idx,item in enumerate(num_list):
                if item % 2 == 0:
                    contador +=1
                    nums += item
            print('El promedio de los numeros pares ingresados es: ',nums/contador)
            os.system('pause')
        
        elif opcion == 'd':
            print('La cantidad de numeros pares ingresados es: ',inCount)
            os.system('pause')
        
        elif opcion == 'e':
            minTen = 0
            for idx,item in enumerate(num_list):
                if item < 10:
                    minTen +=1
            print('La cantidad de numeros menores que 10 es:', minTen)
            os.system('pause')
        
        elif opcion == 'f':
            betNum = 0
            for idx,item in enumerate(num_list):
                if item > 20 and item < 50:
                    betNum +=1
            print('La cantidad de numeros entre 20 y 50 es:', betNum)
            os.system('pause')
        
        elif opcion == 'g':
            ovHundred = 0
            for idx,item in enumerate(num_list):
                if item > 100:
                    ovHundred +=1
            print('La cantidad de numeros mayores a 100 es:', ovHundred)
            os.system('pause')
        
        elif opcion == 'i':
            main()

        else:
            menu_reportes(num_list)

if __name__=='__main__':
    main()