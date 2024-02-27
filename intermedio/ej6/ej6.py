import modulos.registros as rg
import modulos.info as info
def main():
    main_dic = {}
    total_dic = {}
    while True:
        print("""
              +++++++++++++++
              + CONSUMO C02 +
              +++++++++++++++
              """)

        print("""
1. Registrar Dependencia
2. Registrar consumo por dependencia
3. Ver CO2 producido
4. Dependencia que produce mayor CO2
5. Salir
""")

        opcion = solicitar_opcion('Seleccione una opcion: ')
        
        if opcion == 1:
            rg.registro_depedencia(main_dic)
        elif opcion == 2:
            dependencia = input('Ingrese el nombre de la dependencia que desea registrar el consumo: ')
            submenu_registros(main_dic,dependencia)
        elif opcion == 3:
            info.view_table(main_dic,total_dic)
        elif opcion == 4:
            info.find_max(total_dic)
        elif opcion == 5:
            break

def solicitar_opcion(mensaje):
        while True:
            try:
                opcion = int(input(mensaje))
                return opcion
            except ValueError:
                print("Opcion invalida")

def submenu_registros(main_dic,dependencia):
    while True:
        print("""
              ++++++++++++++++++++++++
              + REGISTRO DEPENDENCIA +
              ++++++++++++++++++++++++
              """)

        print("""
1. Registrar consumo electricidad
2. Registrar consumo transporte
3. Registrar consumo por dispositivo
4. Salir
""")

        opcion = solicitar_opcion('Seleccione una opcion: ')
        
        if opcion == 1:
            rg.registro_electricidad(main_dic,dependencia)
        elif opcion == 2:
            rg.registro_transporte(main_dic,dependencia)
        elif opcion == 3:
            rg.registro_dispositivo(main_dic,dependencia)
        elif opcion == 4:
            break




































if __name__ == '__main__':
    main()