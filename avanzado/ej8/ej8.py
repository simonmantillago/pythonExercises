"""
Nivel Avanzado

1. El departamento de bienestar de campus desea organizar un torneo de tenis de mesa y requiere
Un programa que le permita llevar el control de los juegos llevados a cabo por cada uno de los
Inscritos en el torneo. El programa debe cumplir con los siguientes requerimientos:
1. Se tienen 3 categorías (Novato, Intermedio y Avanzado)
2. Cada partido ganado representa 2 puntos para el ganador.
3. Puntos a favor. Los puntos a favor se calculan con los puntos realizados en el juegos restando lo puntos
Recibidos en contra. Ej. Si en el set uno gano 11-7 tiene 4 puntos a favor.
4. El programa debe permitir registrar a cada jugador por categoría.
5. Cada categoría debe tener un mínimo de 5 inscritos para iniciar los juegos en la categoría.
6. En la categoría novatos solo se permiten jugadores entre 15 y 16 años, en intermedio jugadores entre
17 y 20 años y Avanzado jugadores mayores a 20 años.
7. El programa debe permitir llevar un registro detallado de cada jugador. Por ejemplo:

Id Jugador PJ PG PP PA TP
125 Abc 1 1 0 5 2

8. El programa debe permitir conoce el ganador por categoría. En caso de existir un empate el ganador será
El que tenga mas PA(Punto a favor)

El programa debe implementar diccionarios y modulos

"""
players = {}
import os
import experto.modulos.menus as menu
import registro as rg
import game as gm
def main():
    while True:
        os.system('cls')
        op = input(menu.principal)
        if op == '1':
          rg.regis_player(players)  
        if op == '2':
            gm.match(players)
        if op == '3':
            rg.leaderboard(players)
        if op == '4':
            rg.winners(players)
        if op == '5':
            break

if __name__ == '__main__':
    main()