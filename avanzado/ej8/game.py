import os 
import experto.modulos.menus as menu
import registro as rg
import inputs as rs
novatolst = []
intermediolst = []
avanzadolst = []
def match(players):
    if players:
        while (True):
            os.system("cls")
            print("Empezar Los Juegos de la Categoria")
            opMenu = input(menu.categorias)
            if (opMenu == "1"):
                categoryLen("novatos",players)
            elif(opMenu == "2"):
                categoryLen("intermedio",players)
            elif(opMenu == "3"):
                categoryLen("avanzado",players)
            elif(opMenu == "4"):
                break
            else:
                print(menu.error)
            
            os.system("pause")
    else:
        print('No hay jugadores registrados')
        os.system("pause")
def categoryLen(categoria,players):
    gamelst = []
    if categoria == "novatos":
        gamelst = novatolst
    elif categoria == "intermedio":
        gamelst = intermediolst
    elif categoria == "avanzado":
        gamelst = avanzadolst
    
    
    count = 0
    for key,value in players.items():
        if value.get('categoria', 0) == categoria:
            count += 1
            
    if count < 5:  
        print('Hacen falta jugadores para jugar esta categoria')
    elif len(gamelst):
        print('Esta categoria ya jugo')
    else:
        startGame(players,categoria)    

def startGame(players,categoria):
    
    
    gamelst = []
    if categoria == "novatos":
        gamelst = novatolst
    elif categoria == "intermedio":
        gamelst = intermediolst
    elif categoria == "avanzado":
        gamelst = avanzadolst

    count = 0
    for keys,values in players.items():
        if values['categoria'] == categoria: 
            for llave,valor in players.items():
                if keys != llave and (keys,llave) not in gamelst and (llave,keys) not in gamelst:
                    if valor['categoria'] == categoria:
                        count += 1
                        print(f'Partido numero {count} de la categoria {categoria}')
                        print(f'{keys} vs {llave}')
                        puntosK = rs.inputNumber(f'Ingrese los puntos de {keys}')
                        puntosL= rs.inputNumber(f'Ingrese los puntos de {llave}')
                        values['pj'] += 1
                        valor['pj'] += 1
                        if puntosK > puntosL:
                            print(f'El ganador del partido fue {keys}')
                            pa = puntosK - puntosL
                            values['pg'] += 1
                            valor['pp'] +=1
                            values['pa'] += pa
                            values['tp'] +=2
                        elif puntosL > puntosK:
                            print(f'El ganador del partido fue {llave}')
                            pa = puntosL - puntosK
                            valor['pg'] += 1
                            values['pp'] +=1
                            valor['pa'] += pa
                            valor['tp'] +=2
                        else:
                            print("Empate")
                        
                        gamelst.append((keys,llave))
                        gamelst.append((llave,keys))
                        os.system('pause')
                        os.system('cls')
            