import modulos.registro as rg
import modulos.info as info

def main():
    main_dic = {}
    while True:
        rg.os.system('cls')
        print("""
        +++++++++++++++++++++++++++++++
        + ADMINISTRADOR DE INVENTARIO +
        +++++++++++++++++++++++++++++++
              
1. Registro de Productos
2. Visualización de Producto
3. Actualización de Stock
4. Informe de Productos Críticos
5. Cálculo de Ganancia Potencial
6. Salir
              """)

        opcion = solicitar_opcion('Seleccione una opcion: ')
        
        if opcion == 1:
            rg.registrar_producto(main_dic)
        elif opcion == 2:
            info.view_product(main_dic)
        elif opcion == 3:
            info.update_stock(main_dic)
        elif opcion == 4:
            info.low_product(main_dic)
        elif opcion == 5:
            info.earnings(main_dic)
        elif opcion == 6:
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