import modulos.registros as rg
import modulos.info as info

def main():
    main_list = []
    count = 0
    while True:
        rg.os.system('cls')
        print("""
            +++++++++++++++++++
            + SISMOS COLOMBIA +
            +++++++++++++++++++
            """)
        
        print("""
1. Registrar Ciudad
2. Registrar Sismo
3. Buscar sismos por ciudad
4. Informe de riesgo
5. Salir
""")
        
        opcion = solicitar_opcion('Seleccione una opcion: ')
        
        if opcion == 1:
            rg.registro_ciudad(main_list)
            rg.os.system('cls')
        elif opcion == 2:
            while count == 0:
                n = int(input('ingrese el numero de sismo que ingresara por ciudad: '))
                count = n
            rg.registro_sismo(main_list,n)
        elif opcion == 3:
            info.search_city(main_list)
        elif opcion == 4:
            h = info.comprobar(main_list)
            if h == True:
                info.risk_table(main_list)
            else: 
                print('Todas las ciudades registradas deben tener sismos registrados')
                
        elif opcion == 5:
            break

def solicitar_opcion(mensaje):
        while True:
            try:
                opcion = int(input(mensaje))
                return opcion
            except ValueError:
                print("Opcion invalida")

if __name__ == '__main__':
    main()