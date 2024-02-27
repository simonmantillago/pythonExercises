import os
import inputs as rs
import experto.modulos.menus as menu
import game as gm
from tabulate import tabulate

def regis_player(players):
    id_ = str(len(players) + 1).zfill(3)
    player_dic = {
        'Id': id_,
        'nombre': '',
        'edad': '',
        'categoria': '',
        'pj': 0,
        'pg': 0,
        'pp': 0,
        'pa': 0,
        'tp': 0
    }
    player = rs.inputString('Ingrese nombre del jugador')
    player_dic['nombre'] = player
    edad = rs.inputNumber('Ingrese la edad del jugador')
    if edad < 15:
        print(f'El jugador {player_dic['nombre']} debe tener minimo 15 para participar')
        return
    else: 
        player_dic['edad'] = edad
        while True:
            os.system('cls')
            op = input(menu.categorias)
            if op == '1':
                if(not len(gm.novatolst)):
                    if(player_dic['edad'] == 15) or (player_dic['edad'] == 16):
                            player_dic['categoria'] = 'novatos'
                            break
                    else:
                        print("La edad para esta categoria es de 15 a 16 años")
                else:
                     print("Esta categoria ya jugo")
            elif op == '2':
                if(not len(gm.intermediolst)):
                    if(player_dic['edad'] >= 17) and (player_dic['edad'] <= 20):
                            player_dic['categoria'] = 'intermedio'
                            break
                    else:
                        print('La edad para esta categoria es de 17 a 20 años')
                else:
                     print("Esta categoria ya jugo")
            elif op == '3':
                if(not len(gm.avanzadolst)):
                    if(player_dic['edad'] > 20):
                            player_dic['categoria'] = 'avanzado'
                            break
                    else:
                        print('La edad para esta categoria es mas 20 años')
                else:
                     print("Esta categoria ya jugo")
            else:
                print(menu.error)
            os.system('pause')

    if player_dic['categoria']:
        players[player]=player_dic
        print(f'Se Registro el Camper {player_dic['nombre']} en la Categoria {player_dic['categoria']}')
        os.system('pause')


def leaderboard(players):
    sorted_players = sorted(players.values(), key=lambda x: x['categoria'])
    print(tabulate(sorted_players, headers="keys", tablefmt='grid'))
    os.system('pause')

def winners(players):
    
    playersCategory = {}
    
    for keys,values in players.items():
        categoria = values['categoria']
        if categoria not in playersCategory:
            playersCategory[categoria] = [values]
        else:
            playersCategory[categoria].append(values)

    os.system('cls')
    op = input(menu.categorias)
    
    if op == '1':
        wantedCategory = 'novatos'
    elif op == '2':
         wantedCategory = 'intermedio'
    elif op == '3':
         wantedCategory = 'avanzado'

    jugadores_categoria_seleccionada = playersCategory[wantedCategory]
    ganador_categoria = max(jugadores_categoria_seleccionada, key=lambda x: (x['tp'], x['pa']))
    print(f"Ganador en la categoría {wantedCategory}: {ganador_categoria['nombre']} con {ganador_categoria['tp']} puntos y {ganador_categoria['pa']} puntos a favor.")
    os.system('pause')