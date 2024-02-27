import os
from tabulate import tabulate

def main():
    student_list = []
    while True:
        print("""
        ++++++++++++++++++++++
        + Calculadora de IMC +
        ++++++++++++++++++++++
    """)
        print('1. Añadir estudiante')
        print('2. Lista de estudiantes')
        print('3. Reportes')
        
        option = input('Seleccione una opcion: ')
        if option == '1':
            add_student(student_list)
        elif option == '2':
            view_alumno(student_list)
        elif option == '3':
            menu_info(student_list)
        else: 
            break

def obtener_numero(mensaje):
    while True:
        try:
            numero = float(input(mensaje))
            if numero < 0:
                print("Dato invalido")
                os.system('clear')
            else:
                return numero
        except ValueError:
            print("Dato invalido")

def add_student(student_list):
    name = input('Ingrese el nombre del estudiante: ')
    age = int(input(f'Ingrese la edad del estudiante {name}: '))
    weight = obtener_numero(f'Ingrese el peso de {name}: ')
    height = obtener_numero(f'Ingrese la altura de {name}: ')
    imc = weight / (height ** 2)
     
    if 18.5 <= imc <= 24.9:
        category = 'Normal'
    elif 25 <= imc <= 29.9:
        category = 'Sobrepeso'
    elif 30 <= imc <= 34.9:
        category = 'Obesidad 1'
    elif 35 <= imc <= 39.9:
        category = 'Obesidad 2'
    elif imc >= 40:
        category = 'Obesidad 3'
    else:
        category = 'No califica'
    
    idx_alumnos(student_list, name, age, weight, height, imc, category)

def idx_alumnos(student_list, nombre_alumno, age, weight, height, imc, category):
    nuevo_alumno = [nombre_alumno, age, weight, height, imc, category]  
    student_list.append(nuevo_alumno)

def view_alumno(student_list):
    if student_list:
        titulo ="""
        ++++++++++++++++++++++++++++++++++++++
        + LISTADO DEL IMC DE LOS ESTUDIANTES +
        ++++++++++++++++++++++++++++++++++++++
        """
        print(titulo)
        print(tabulate(student_list, headers=['Nombre', 'Edad', 'Peso', 'Altura', 'IMC', 'Categoria'], tablefmt='grid'))
    else:
        print("No hay información disponible. Registre alumnos primero.")

def menu_info(student_list):
    while True:
        print("""
        ++++++++++++++++++++++
        + Calculadora de IMC +
        ++++++++++++++++++++++
    """)
        print('1. Numero de estudiantes se encuentran en el peso ideal')
        print('2. Numero de estudiantes se encuentran en Obesidad 1')
        print('3. Numero de estudiantes se encuentran en Obesidad 2')
        print('4. Numero de estudiantes se encuentran en Obesidad 3')
        print('5. Numero de estudiantes se encuentran en sobrepeso')
        print('6. Volver')
        
        
        option = input('Seleccione una opcion: ')
        if option == '1':
            sumar_imc_normal(student_list)
        elif option == '2':
            sumar_imc_obesidad_1(student_list)
        elif option == '3':
            sumar_imc_obesidad_2(student_list)
        elif option == '4':
            sumar_imc_obesidad_3(student_list)
        elif option == '5':
            sumar_imc_sobrepeso(student_list)
        elif option == '6':
            main()
        else: 
            break

def sumar_imc_normal(student_list):
    suma_imc_normal = 0
    for student in student_list:
        if student[5] == 'Normal':  
            suma_imc_normal += 1  
    print("La suma de los IMC de estudiantes con categoría 'Normal' es:", suma_imc_normal)

def sumar_imc_obesidad_1(student_list):
    sumar_imc_obesidad_1 = 0
    for student in student_list:
        if student[5] == 'Obesidad 1':  # La categoría está en la posición 5 de la lista
            sumar_imc_obesidad_1 += 1  # El IMC está en la posición 4 de la lista
    print("La suma de los IMC de estudiantes con categoría 'Obesidad 13' es:", sumar_imc_obesidad_1)

def sumar_imc_obesidad_2(student_list):
    sumar_imc_obesidad_2 = 0
    for student in student_list:
        if student[5] == 'Obesidad 2':  # La categoría está en la posición 5 de la lista
            sumar_imc_obesidad_2 += 1  # El IMC está en la posición 4 de la lista
    print("La suma de los IMC de estudiantes con categoría 'Obesidad 2' es:", sumar_imc_obesidad_2)

def sumar_imc_obesidad_3(student_list):
    sumar_imc_obesidad_3 = 0
    for student in student_list:
        if student[5] == 'Obesidad 3':  # La categoría está en la posición 5 de la lista
            sumar_imc_obesidad_3 += 1  # El IMC está en la posición 4 de la lista
    print("La suma de los IMC de estudiantes con categoría 'Obesidad 3' es:", sumar_imc_obesidad_3)

def sumar_imc_sobrepeso(student_list):
    sumar_imc_sobrepeso = 0
    for student in student_list:
        if student[5] == 'Sobrepeso':  # La categoría está en la posición 5 de la lista
            sumar_imc_sobrepeso+= 1  # El IMC está en la posición 4 de la lista
    print("La suma de los IMC de estudiantes con categoría 'Obesidad 2' es:", sumar_imc_sobrepeso)


if __name__ == "__main__":
    main()
