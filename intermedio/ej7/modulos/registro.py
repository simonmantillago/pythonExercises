import os

def registrar_producto(main_dic):
    producto = input('Ingrese el nombre del producto: ')
    codigo = input('Ingrese el codigo del producto: ').zfill(6)
    nombre = producto
    valor_compra = float(input(f'Ingrese el valor de compra de {nombre}: '))
    valor_venta = float(input(f'Ingrese el valor de venta de {nombre}: '))
    min_stock = float(input(f'Ingrese la cantidad minima que debe haber de {nombre} en stock: '))
    max__stock = float(input(f'Ingrese la cantidad maxima que debe haber de {nombre} en stock: '))
    stock = float(input(f'Ingrese la cantidad actual de {nombre} en stock: '))
    nombre_prov = input(f'Ingrese el nombre del provedor de {nombre}: ')
    
    producto_dic = {
        'Codigo' : codigo,
        'Nombre': producto,
        'Valor_compra' : valor_compra,
        'Valor_venta' : valor_venta,
        'Min_Stock' : min_stock,
        'Max_Stock' : max__stock,
        'Stock_actual': stock,
        'Proveedor' : nombre_prov
    }
    main_dic[producto]=producto_dic
    print('Producto registrado correctamente')
    
    os.system('pause')