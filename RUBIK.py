from collections import deque
from queue import PriorityQueue
import random

# Definimos los colores
BLANCO = 'Blanco'
VERDE = 'Verde'
NARANJA = 'Naranja'
ROJO = 'Rojo'
AMARILLO = 'Amarillo'
AZUL = 'Azul'

class CuboRubik:
    def __init__(self):
        self.cubo = {
            'U': [[BLANCO, BLANCO, BLANCO], [BLANCO, BLANCO, BLANCO], [BLANCO, BLANCO, BLANCO]],
            'F': [[VERDE, VERDE, VERDE], [VERDE, VERDE, VERDE], [VERDE, VERDE, VERDE]],
            'L': [[NARANJA, NARANJA, NARANJA], [NARANJA, NARANJA, NARANJA], [NARANJA, NARANJA, NARANJA]],
            'R': [[ROJO, ROJO, ROJO], [ROJO, ROJO, ROJO], [ROJO, ROJO, ROJO]],
            'D': [[AMARILLO, AMARILLO, AMARILLO], [AMARILLO, AMARILLO, AMARILLO], [AMARILLO, AMARILLO, AMARILLO]],
            'B': [[AZUL, AZUL, AZUL], [AZUL, AZUL, AZUL], [AZUL, AZUL, AZUL]]
        }
        self.movimientos = []

    def cargar_configuracion(self, archivo):
        with open(archivo, 'r') as file:
            for linea, cara in zip(file, self.cubo.keys()):
                colores = linea.strip().split(',')
                for i in range(3):
                    self.cubo[cara][i] = colores[i*3:i*3+3]

    def mostrar_cubo(self):
        for cara, colores in self.cubo.items():
            print(cara)
            for fila in colores:
                print(fila)
            print()

    def aplicar_movimiento(self, estado, movimiento):
        # Realiza una copia del estado actual para no modificarlo directamente
        nuevo_estado = {cara: [fila[:] for fila in colores] for cara, colores in estado.items()}

        if movimiento == 'U':
            nuevo_estado['U'][0], nuevo_estado['U'][1], nuevo_estado['U'][2] = nuevo_estado['U'][2], nuevo_estado['U'][0], nuevo_estado['U'][1]
            nuevo_estado['F'][0][0], nuevo_estado['R'][0][0], nuevo_estado['B'][0][0], nuevo_estado['L'][0][0] = nuevo_estado['L'][0][0], nuevo_estado['F'][0][0], nuevo_estado['R'][0][0], nuevo_estado['B'][0][0]
            nuevo_estado['F'][0][1], nuevo_estado['R'][0][1], nuevo_estado['B'][0][1], nuevo_estado['L'][0][1] = nuevo_estado['L'][0][1], nuevo_estado['F'][0][1], nuevo_estado['R'][0][1], nuevo_estado['B'][0][1]
            nuevo_estado['F'][0][2], nuevo_estado['R'][0][2], nuevo_estado['B'][0][2], nuevo_estado['L'][0][2] = nuevo_estado['L'][0][2], nuevo_estado['F'][0][2], nuevo_estado['R'][0][2], nuevo_estado['B'][0][2]

        elif movimiento == 'U\'':
            nuevo_estado['U'][0], nuevo_estado['U'][1], nuevo_estado['U'][2] = nuevo_estado['U'][1], nuevo_estado['U'][2], nuevo_estado['U'][0]
            nuevo_estado['F'][0][0], nuevo_estado['R'][0][0], nuevo_estado['B'][0][0], nuevo_estado['L'][0][0] = nuevo_estado['R'][0][0], nuevo_estado['B'][0][0], nuevo_estado['L'][0][0], nuevo_estado['F'][0][0]
            nuevo_estado['F'][0][1], nuevo_estado['R'][0][1], nuevo_estado['B'][0][1], nuevo_estado['L'][0][1] = nuevo_estado['R'][0][1], nuevo_estado['B'][0][1], nuevo_estado['L'][0][1], nuevo_estado['F'][0][1]
            nuevo_estado['F'][0][2], nuevo_estado['R'][0][2], nuevo_estado['B'][0][2], nuevo_estado['L'][0][2] = nuevo_estado['R'][0][2], nuevo_estado['B'][0][2], nuevo_estado['L'][0][2], nuevo_estado['F'][0][2]

        elif movimiento == 'F':
            nuevo_estado['F'][0], nuevo_estado['F'][1], nuevo_estado['F'][2] = nuevo_estado['F'][2], nuevo_estado['F'][0], nuevo_estado['F'][1]
            nuevo_estado['U'][2][0], nuevo_estado['R'][0][0], nuevo_estado['D'][0][2], nuevo_estado['L'][2][2] = nuevo_estado['L'][2][2], nuevo_estado['U'][2][0], nuevo_estado['R'][0][0], nuevo_estado['D'][0][2]
            nuevo_estado['U'][2][1], nuevo_estado['R'][0][1], nuevo_estado['D'][1][2], nuevo_estado['L'][1][2] = nuevo_estado['L'][1][2], nuevo_estado['U'][2][1], nuevo_estado['R'][0][1], nuevo_estado['D'][1][2]
            nuevo_estado['U'][2][2], nuevo_estado['R'][0][2], nuevo_estado['D'][2][2], nuevo_estado['L'][0][2] = nuevo_estado['L'][0][2], nuevo_estado['U'][2][2], nuevo_estado['R'][0][2], nuevo_estado['D'][2][2]

        elif movimiento == 'L':
            nuevo_estado['L'][0], nuevo_estado['L'][1], nuevo_estado['L'][2] = nuevo_estado['L'][2], nuevo_estado['L'][0], nuevo_estado['L'][1]
            nuevo_estado['U'][0][0], nuevo_estado['B'][0][0], nuevo_estado['D'][0][0], nuevo_estado['F'][0][0] = nuevo_estado['F'][0][0], nuevo_estado['U'][0][0], nuevo_estado['B'][0][0], nuevo_estado['D'][0][0]
            nuevo_estado['U'][1][0], nuevo_estado['B'][1][0], nuevo_estado['D'][1][0], nuevo_estado['F'][1][0] = nuevo_estado['F'][1][0], nuevo_estado['U'][1][0], nuevo_estado['B'][1][0], nuevo_estado['D'][1][0]
            nuevo_estado['U'][2][0], nuevo_estado['B'][2][0], nuevo_estado['D'][2][0], nuevo_estado['F'][2][0] = nuevo_estado['F'][2][0], nuevo_estado['U'][2][0], nuevo_estado['B'][2][0], nuevo_estado['D'][2][0]

        elif movimiento == 'L\'':
            nuevo_estado['L'][0], nuevo_estado['L'][1], nuevo_estado['L'][2] = nuevo_estado['L'][1], nuevo_estado['L'][2], nuevo_estado['L'][0]
            nuevo_estado['U'][0][0], nuevo_estado['B'][0][0], nuevo_estado['D'][0][0], nuevo_estado['F'][0][0] = nuevo_estado['B'][0][0], nuevo_estado['D'][0][0], nuevo_estado['F'][0][0], nuevo_estado['U'][0][0]
            nuevo_estado['U'][1][0], nuevo_estado['B'][1][0], nuevo_estado['D'][1][0], nuevo_estado['F'][1][0] = nuevo_estado['B'][1][0], nuevo_estado['D'][1][0], nuevo_estado['F'][1][0], nuevo_estado['U'][1][0]
            nuevo_estado['U'][2][0], nuevo_estado['B'][2][0], nuevo_estado['D'][2][0], nuevo_estado['F'][2][0] = nuevo_estado['B'][2][0], nuevo_estado['D'][2][0], nuevo_estado['F'][2][0], nuevo_estado['U'][2][0]

        elif movimiento == 'R':
            nuevo_estado['R'][0], nuevo_estado['R'][1], nuevo_estado['R'][2] = nuevo_estado['R'][2], nuevo_estado['R'][0], nuevo_estado['R'][1]
            nuevo_estado['U'][0][2], nuevo_estado['F'][0][2], nuevo_estado['D'][0][2], nuevo_estado['B'][0][2] = nuevo_estado['B'][0][2], nuevo_estado['U'][0][2], nuevo_estado['F'][0][2], nuevo_estado['D'][0][2]
            nuevo_estado['U'][1][2], nuevo_estado['F'][1][2], nuevo_estado['D'][1][2], nuevo_estado['B'][1][2] = nuevo_estado['B'][1][2], nuevo_estado['U'][1][2], nuevo_estado['F'][1][2], nuevo_estado['D'][1][2]
            nuevo_estado['U'][2][2], nuevo_estado['F'][2][2], nuevo_estado['D'][2][2], nuevo_estado['B'][2][2] = nuevo_estado['B'][2][2], nuevo_estado['U'][2][2], nuevo_estado['F'][2][2], nuevo_estado['D'][2][2]

        elif movimiento == 'R\'':
            nuevo_estado['R'][0], nuevo_estado['R'][1], nuevo_estado['R'][2] = nuevo_estado['R'][1], nuevo_estado['R'][2], nuevo_estado['R'][0]
            nuevo_estado['U'][0][2], nuevo_estado['F'][0][2], nuevo_estado['D'][0][2], nuevo_estado['B'][0][2] = nuevo_estado['F'][0][2], nuevo_estado['D'][0][2], nuevo_estado['B'][0][2], nuevo_estado['U'][0][2]
            nuevo_estado['U'][1][2], nuevo_estado['F'][1][2], nuevo_estado['D'][1][2], nuevo_estado['B'][1][2] = nuevo_estado['F'][1][2], nuevo_estado['D'][1][2], nuevo_estado['B'][1][2], nuevo_estado['U'][1][2]
            nuevo_estado['U'][2][2], nuevo_estado['F'][2][2], nuevo_estado['D'][2][2], nuevo_estado['B'][2][2] = nuevo_estado['F'][2][2], nuevo_estado['D'][2][2], nuevo_estado['B'][2][2], nuevo_estado['U'][2][2]

        elif movimiento == 'D':
            nuevo_estado['D'][0], nuevo_estado['D'][1], nuevo_estado['D'][2] = nuevo_estado['D'][2], nuevo_estado['D'][0], nuevo_estado['D'][1]
            nuevo_estado['F'][2][0], nuevo_estado['R'][2][0], nuevo_estado['B'][2][0], nuevo_estado['L'][2][0] = nuevo_estado['L'][2][0], nuevo_estado['F'][2][0], nuevo_estado['R'][2][0], nuevo_estado['B'][2][0]
            nuevo_estado['F'][2][1], nuevo_estado['R'][2][1], nuevo_estado['B'][2][1], nuevo_estado['L'][2][1] = nuevo_estado['L'][2][1], nuevo_estado['F'][2][1], nuevo_estado['R'][2][1], nuevo_estado['B'][2][1]
            nuevo_estado['F'][2][2], nuevo_estado['R'][2][2], nuevo_estado['B'][2][2], nuevo_estado['L'][2][2] = nuevo_estado['L'][2][2], nuevo_estado['F'][2][2], nuevo_estado['R'][2][2], nuevo_estado['B'][2][2]

        elif movimiento == 'D\'':
            nuevo_estado['D'][0], nuevo_estado['D'][1], nuevo_estado['D'][2] = nuevo_estado['D'][1], nuevo_estado['D'][2], nuevo_estado['D'][0]
            nuevo_estado['F'][2][0], nuevo_estado['R'][2][0], nuevo_estado['B'][2][0], nuevo_estado['L'][2][0] = nuevo_estado['R'][2][0], nuevo_estado['B'][2][0], nuevo_estado['L'][2][0], nuevo_estado['F'][2][0]
            nuevo_estado['F'][2][1], nuevo_estado['R'][2][1], nuevo_estado['B'][2][1], nuevo_estado['L'][2][1] = nuevo_estado['R'][2][1], nuevo_estado['B'][2][1], nuevo_estado['L'][2][1], nuevo_estado['F'][2][1]
            nuevo_estado['F'][2][2], nuevo_estado['R'][2][2], nuevo_estado['B'][2][2], nuevo_estado['L'][2][2] = nuevo_estado['R'][2][2], nuevo_estado['B'][2][2], nuevo_estado['L'][2][2], nuevo_estado['F'][2][2]

        elif movimiento == 'B':
            nuevo_estado['B'][0], nuevo_estado['B'][1], nuevo_estado['B'][2] = nuevo_estado['B'][2], nuevo_estado['B'][0], nuevo_estado['B'][1]
            nuevo_estado['U'][0][0], nuevo_estado['R'][0][0], nuevo_estado['D'][0][0], nuevo_estado['L'][0][0] = nuevo_estado['R'][0][0], nuevo_estado['D'][0][0], nuevo_estado['L'][0][0], nuevo_estado['U'][0][0]
            nuevo_estado['U'][0][1], nuevo_estado['R'][0][1], nuevo_estado['D'][0][1], nuevo_estado['L'][0][1] = nuevo_estado['R'][0][1], nuevo_estado['D'][0][1], nuevo_estado['L'][0][1], nuevo_estado['U'][0][1]
            nuevo_estado['U'][0][2], nuevo_estado['R'][0][2], nuevo_estado['D'][0][2], nuevo_estado['L'][0][2] = nuevo_estado['R'][0][2], nuevo_estado['D'][0][2], nuevo_estado['L'][0][2], nuevo_estado['U'][0][2]

        elif movimiento == 'B\'':
            nuevo_estado['B'][0], nuevo_estado['B'][1], nuevo_estado['B'][2] = nuevo_estado['B'][1], nuevo_estado['B'][2], nuevo_estado['B'][0]
            nuevo_estado['U'][0][0], nuevo_estado['R'][0][0], nuevo_estado['D'][0][0], nuevo_estado['L'][0][0] = nuevo_estado['L'][0][0], nuevo_estado['U'][0][0], nuevo_estado['R'][0][0], nuevo_estado['D'][0][0]
            nuevo_estado['U'][0][1], nuevo_estado['R'][0][1], nuevo_estado['D'][0][1], nuevo_estado['L'][0][1] = nuevo_estado['L'][0][1], nuevo_estado['U'][0][1], nuevo_estado['R'][0][1], nuevo_estado['D'][0][1]
            nuevo_estado['U'][0][2], nuevo_estado['R'][0][2], nuevo_estado['D'][0][2], nuevo_estado['L'][0][2] = nuevo_estado['L'][0][2], nuevo_estado['U'][0][2], nuevo_estado['R'][0][2], nuevo_estado['D'][0][2]
        self.mostrar_cubo()
        return nuevo_estado
        

    def resolver_cubo(self):
        cola = deque([(self.cubo, [])])

        while cola:
            estado, pasos = cola.popleft()

            if self.es_solucion(estado):
                self.movimientos = pasos
                return True

            for movimiento in self.generar_movimientos_posibles():
                nuevo_estado = self.aplicar_movimiento(estado, movimiento)
                cola.append((nuevo_estado, pasos + [movimiento]))

        return False

    def busqueda_optima(self):
        # Definir la función heurística
        def heuristica(estado):
            # Heurística: Contar la cantidad de cubos mal ubicados en cada cara
            mal_ubicados = 0
            for colores in estado.values():
                for fila in colores:
                    mal_ubicados += sum(1 for color in fila if color != fila[0])
            return mal_ubicados

        # Inicializar la cola de prioridad con el estado inicial y una estimación inicial
        cola_prioridad = PriorityQueue()
        cola_prioridad.put((0, self.cubo, []))  # (estimación, estado, pasos)

        # Conjunto para almacenar los estados ya visitados
        visitados = set()

        while not cola_prioridad.empty():
            _, estado, pasos = cola_prioridad.get()

            # Verificar si hemos llegado al estado objetivo
            if self.es_solucion(estado):
                self.movimientos = pasos
                return True

            # Generar movimientos posibles y aplicarlos al estado actual
            for movimiento in self.generar_movimientos_posibles():
                nuevo_estado = self.aplicar_movimiento(estado, movimiento)

                # Verificar si el nuevo estado ya ha sido visitado
                if nuevo_estado in visitados:
                    continue

                # Calcular la nueva estimación y agregar el estado a la cola de prioridad
                nueva_estimacion = heuristica(nuevo_estado) + len(pasos)
                cola_prioridad.put((nueva_estimacion, nuevo_estado, pasos + [movimiento]))

                # Agregar el nuevo estado al conjunto de visitados
                visitados.add(nuevo_estado)

        return False

    def es_solucion(self, estado):
        # Verifica si todas las caras del cubo tienen un solo color
        for colores in estado.values():
            if len(set(colores[0])) != 1 or len(set(colores[1])) != 1 or len(set(colores[2])) != 1:
                return False
        return True

    def generar_movimientos_posibles(self):
        return ['U', 'U\'', 'F', 'F\'', 'L', 'L\'', 'R', 'R\'', 'D', 'D\'', 'B', 'B\'']

    def mezclar_cubo(self):
     movimientos = ['U', 'U\'', 'F', 'F\'', 'L', 'L\'', 'R', 'R\'', 'D', 'D\'', 'B', 'B\'']
     for _ in range(20):
        movimiento = random.choice(movimientos)
        print(f'Aplicando movimiento: {movimiento}')
        self.cubo = self.aplicar_movimiento(self.cubo, movimiento)  # Corregir aquí
        self.mostrar_cubo()
        input("Presiona Enter para continuar...")

if __name__ == "__main__":
    cubo = CuboRubik()
    while True:
        input("Presiona Enter para mezclar el cubo...")
        cubo.mezclar_cubo()  # Llama a la función mezclar_cubo antes de mostrar el cubo
        cubo.mostrar_cubo()
        if input("¿Deseas resolver el cubo? (si/no): ").lower() == 'si':
            if cubo.resolver_cubo():
                print("Solución encontrada:")
                print(cubo.movimientos)
                print("Cantidad de pasos:", len(cubo.movimientos))
                break
            else:
                print("No se encontró solución.")
        else:
            for _ in range(5):
                input("Presiona Enter para mezclar el cubo...")
                cubo.mezclar_cubo()  # Llama a la función mezclar_cubo antes de mostrar el cubo
                cubo.mostrar_cubo()
                if input("¿Deseas resolver el cubo? (si/no): ").lower() == 'si':
                    if cubo.resolver_cubo():
                        print("Solución encontrada:")
                        print(cubo.movimientos)
                        print("Cantidad de pasos:", len(cubo.movimientos))
                        break
                    else:
                        print("No se encontró solución.")
            else:
                continue
            break