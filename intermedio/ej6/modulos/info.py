import os
def view_table(main_dic,total_dic):
    nombre_dependencia = input('Ingrese el nombre de la dependencia que desea ver: ')
    if nombre_dependencia in main_dic:
        
        dependencia_dic = main_dic[nombre_dependencia]
        
        consumo_electricidad = dependencia_dic.get('consumo_electricidad', 0)
        transporte = dependencia_dic.get('transporte', 0)
        for idx,item in enumerate(dependencia_dic.get('dispositivos', [0])):
            valor = item

        dispositivos = valor
        if consumo_electricidad == type:
            co_total= consumo_electricidad + dispositivos + transporte
        else:
            co_total=  dispositivos + transporte
        
        total_dic[nombre_dependencia] = co_total
        
        print(f"Emisiones de CO2 de {nombre_dependencia}: {co_total}")
        os.system('pause')
        os.system('cls')
    
    else:
        print(f"La dependencia '{nombre_dependencia}' no existe en el registro.")
        os.system('pause')
        os.system('cls')
    


def find_max(total_dic):
    max_valor = max(total_dic.values())
    clave_max_valor = max(total_dic, key=total_dic.get)

    print(f'{clave_max_valor} es la dependencia que mas produce C02 con un emision de {max_valor}')
    os.system('pause')
    os.system('cls')
    