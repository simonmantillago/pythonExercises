import os
def registro_ciudad(main_list):
    if len(main_list) <= 5:
        new_city = input('Ingrese la ciudad que desea registrar: ')
        city = [new_city]
        main_list.append(city)
        print('Ciudad registrada corrrectamente')
        os.system('pause')
    else:
        print('maximo se pueden ingresar 5 ciudades')
        os.system('pause')

def registro_sismo(main_list,n):
    city_sismo = input('Ingrese la ciudad en la que ocurrio el sismo: ')
    city_found = False
    for idx, item in enumerate(main_list):
        if item[0] == city_sismo:
            city_found = True
            while (len(main_list[idx])-1) < n:
                sismo = float(input('Ingrese la magnitud del sismo: '))
                item.append(sismo)
                
        
        if not city_found:
            print('Ciudad no registrada')

