import random

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class Lista_Circular(object):
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def length(self):
        cur = self.head
        count = 0
        while cur is not None:
            count += 1
            if cur.next == self.head:
                break
            else:
                cur = cur.next
        return count

    def add_head(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            new_node.next = self.head
        else:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            # El nodo de cola apunta al nuevo nodo
            cur.next = new_node
            # El nuevo nodo apunta al nodo principal original
            new_node.next = self.head
            # Luego dele el título del nodo principal al nuevo nodo
            self.head = new_node

    def add_last(self, data):
        node = Node(data)
        if self.is_empty():
            self.head = node
            node.next = self.head
        else:
            cur = self.head
            # Mueve el puntero al final
            while cur.next != self.head:
                cur = cur.next
            # El nodo de cola apunta al nuevo nodo
            cur.next = node
            # El nuevo nodo apunta al nodo principal
            node.next = self.head

    def remove_node(self, data):
        if self.is_empty():
            return
        elif data == self.head.data:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = self.head.next
            self.head = self.head.next
        else:
            cur = self.head
            pre = None
            while cur.data != data:
                pre = cur
                cur = cur.next
            pre.next = cur.next

    def display(self):
        nodes = []
        cur = self.head
        while cur:
            nodes.append(cur.data)
            if cur.next == self.head:
                break
            cur = cur.next
        print(" -> ".join(map(str, nodes)))

# Función para lanzar dos dados
def lanzar_dados():
    return random.randint(1, 6), random.randint(1, 6)

# Crear la lista circular con los nombres de 5 jugadores
jugadores = Lista_Circular()
nombres = ["Jugador1", "Jugador2", "Jugador3", "Jugador4", "Jugador5"]
for nombre in nombres:
    jugadores.add_last({"nombre": nombre, "acumulado": 0})

# Simulación del juego de dados
def juego_dados(jugadores):
    cur = jugadores.head
    while True:
        nombre = cur.data["nombre"]
        acumulado = cur.data["acumulado"]
        dado1, dado2 = lanzar_dados()
        suma = dado1 + dado2
        print(f"{nombre} lanza los dados: {dado1} y {dado2} (Suma: {suma})")

        # Si saca dobles, es el ganador
        if dado1 == dado2:
            print(f"{nombre} ha sacado dobles y es el ganador!")
            break

        # Si la suma es superior o igual a 10, eliminar al jugador
        if suma >= 10:
            print(f"{nombre} ha sido eliminado por sacar una suma de {suma}.")
            siguiente = cur.next
            jugadores.remove_node(cur.data)
            cur = siguiente
            if jugadores.length() == 1:
                print(f"{cur.data['nombre']} es el último jugador y gana por defecto.")
                break
            continue

        # Si la suma es igual a 7, mover al jugador al final de la lista
        if suma == 7:
            print(f"{nombre} se mueve al final de la lista por sacar una suma de 7.")
            jugadores.remove_node(cur.data)
            jugadores.add_last(cur.data)
            cur = cur.next
            continue

        # Acumular los puntos del jugador
        cur.data["acumulado"] += suma

        # Preguntar al usuario si desea finalizar el juego
        finalizar = input("¿Desea finalizar el juego? (s/n): ")
        if finalizar.lower() == 's':
            print("Juego finalizado. Acumulado de puntos:")
            jugadores.display()
            break

        cur = cur.next

# Iniciar el juego
juego_dados(jugadores)