from tabulate import tabulate
import os
def view_product(main_dic):
    data = list(main_dic.values())
    print(tabulate(data, headers="keys",tablefmt='grid'))
    os.system('pause')

def update_stock(main_dic):
    llave = input('Ingrese el producto del que desea actualizar: ')
    stock = float(input('Ingrese la cantidad de stock del producto: '))
    main_dic[llave]['Stock_actual'] = stock

def low_product(main_dic):
    print("""
+++++++ Productos en estado critico ++++++++++
""")
    for producto, value in main_dic.items():
        stock_actual = value.get('Stock_actual', 0)
        min_stock = value.get('Min_Stock', 0)  
        
        if stock_actual < min_stock:  
            print(f'{producto} con un minimo stock de {min_stock} cuenta con un stock de: {stock_actual}')
    os.system('pause')

def earnings(main_dic):
    producto = input('Ingrese el nombre del producto que desea consultar: ')
    for key, value in main_dic.items():
        if producto == key:
            stock_actual = value.get('Stock_actual', 0)
            valor_venta = value.get('Valor_venta', 0)
            valor_compra = value.get('Valor_compra',0)
            earning = (valor_venta - valor_compra)* stock_actual
            os.system('cls')
            print(f"""
Producto: {producto}
Stock: {stock_actual}
Precio compra: ${valor_compra}
Precio venta: ${valor_venta}
Ganancias potenciales: ${earning}
""")
    os.system('pause')