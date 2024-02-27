import os
from tabulate import tabulate

def search_city(main_list):
    
    city_name = input('Ingrese la ciudad de la que desea consultar los sismos: ')
    city_found = False
    os.system('cls')
    for idx, item in enumerate(main_list):
        city_found = True
        if item[0] == city_name:
            print(f'Sismos de {item[0]}:')
            for i, value in enumerate(item[1:], start=1):
                print(f"Sismo {i}: {value}")
            os.system('pause')
            break
                
    if not city_found:
        print('Ciudad no registrada')
        os.system('pause')
    
def risk_table(main_list):

    table_list = []
    for idx, item in enumerate(main_list):
        count = 0
        sis_count = 0
        risk = ''
        city_name = item[0]
        for i, value in enumerate(item[1:], start=1):
            sis_count += value
            count += 1
            average = round(sis_count/count,2)
            if average <= 2.5:
                risk = 'Amarillo'
            elif average > 2.5 and average <= 4.5:
                risk = 'Naranja'
            elif average > 4.5:
                risk = 'Rojo'

        sub_table = [city_name,average,risk]
        table_list.append(sub_table)
    
    if table_list:
        table_list.sort(key=lambda item: item[1])
        titulo ="""
        ++++++++++++++++++++++++++++++++++
        + TABLA DE RIEGO SISMOS COLOMBIA +
        ++++++++++++++++++++++++++++++++++
        """
        print(titulo)
        print(tabulate(table_list,headers=['CIUDAD','PROMEDIO SISMOS','NIVEL DE RIEGO'],tablefmt='grid'))
        os.system('pause')
    else:
        print("No hay información disponible. Registre ciudades primero")

def comprobar(ciudades:list):
    primeraLista = len(ciudades[0])
    for listas in ciudades[1:]:
        if len(listas) != primeraLista:
            return False
    return True