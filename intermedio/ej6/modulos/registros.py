import os
def registro_depedencia(main_dic):
    dependencia = input('Ingrese el nombre de la dependencia: ')
    dependencia_dic = {
        'consumo_electricidad' : float,
        'transporte': float,
        'dispositivos' : []
    }
    
    main_dic[dependencia]=dependencia_dic
    print('Dependencia registrada exitosamente')
    os.system('pause')
    os.system('cls')
    
    

def registro_electricidad(main_dic,dependencia):
    kWh = float(input('Ingrese la cantida de kWh que se encuentra en tu factura: '))
    tiempo = float(input('Cuanto tiempo de consumo en meses registra tu factura: '))
    factor_consumo = tipo_consumo()
    
    if tiempo > 1:
        consumo_mensual = kWh/tiempo
        emision = consumo_mensual * factor_consumo
    else: 
        consumo_mensual = kWh
        emision = consumo_mensual * factor_consumo
    
            
    
    main_dic[dependencia]['consumo_electricidad'] = emision
    
    
def registro_transporte(main_dic,dependencia):
   
    km = float(input('Ingrese la cantida de km que recorridos en el transporte: '))
    factor_consumo = tipo_consumo()
    
    emision = km / factor_consumo
    main_dic[dependencia]['transporte'] = round(emision,2)
        
    
def registro_dispositivo(main_dic,dependencia):
    
    potencia = float(input('Ingrese la potencia del dispositivo a registrar: '))
    tiempo_hora = float(input('Ingrese la cantidad de horas diarias del uso del dispositivo: '))*30
    factor_consumo = tipo_consumo()
    consumo_total = (potencia * tiempo_hora)/1000
    
    emision = consumo_total * factor_consumo
    
    if len(main_dic[dependencia]['dispositivos']) > 0:
        suma_dispositivos = sum(main_dic[dependencia]['dispositivos'])
        main_dic[dependencia]['dispositivos'] = [suma_dispositivos]
    else:
        main_dic[dependencia]['dispositivos'].append(emision)
        
    

def tipo_consumo():
    factor_consumo = (input('Cual es la fuente de energia utilizada Hidraulica(h) , Termica(t), No convencional(n):'))
    if factor_consumo == 'h':
        factor = 0
        
    elif factor_consumo == 't':
        factor = 0.3
        
    elif factor_consumo == 'n':
        factor = 0.1
    return factor