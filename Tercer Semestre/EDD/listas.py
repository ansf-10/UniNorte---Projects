class Nodo:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next


class Lista_enlazada:
    def __init__(self):
        self.head = None

    # Método para agregar elementos en el frente de la linked list
    def agregar_al_inicio(self, data):
        self.head = Nodo(data=data, next=self.head)
        

    # Método para verificar si la estructura de datos esta vacia
    def is_empty(self):
        return self.head == None

    # Método para agregar elementos al final de la lista enlazada
    def agregar_al_final(self, data):
      #Si la lista no existe, entonces se crea
        if not self.head:
            self.head = Nodo(data=data)
            return
        #recorre toda la lista hasta llegar al final,
        #cuando temporal.next=None
        temporal = self.head
        while temporal.next:
            temporal = temporal.next
        #Cuando llega al final de la lista, enlaza el último nodo con
        #el nuevo nodo que se crea
        temporal.next = Nodo(data=data)

    # Método para eleminar nodos
    def delete_node(self, key):
        actual = self.head
        previo = None
        #Se busca el dato a eliminar en la lista
        while actual and actual.data != key:
            previo = actual
            actual = actual.next
        #Si el dato a eliminar es el primero,
        #entonces se reasigna la cabeza de la lista
        if previo is None:
            self.head = actual.next
        elif actual:
            previo.next = actual.next
            actual.next = None

    # Método para obtener el ultimo nodo
    def get_last_node(self):
        temp = self.head
        while(temp.next is not None):
            temp = temp.next
        return temp.data

    # Método para imprimir la lista de nodos
    def print_list( self ):
        node = self.head
        while node != None:
            print(node.data, end =" --> ")
            node = node.next

    # Método para insertar dato
    def insertar_dato(self, data):
        if not isinstance(data, (int, float)):
            print("El dato debe ser un número.")
            return

        if self.existente(data):
            print("El dato ya se encuentra en la lista.")
            return

        if data < 0:
            self.agregar_al_inicio(data)
        elif data > 0:
            self.agregar_al_final(data)
        else:
            if self.is_empty():
                self.head = Nodo(data=data)
            else:
                temporal = self.head
                while temporal.next and temporal.next.data < 0:
                    temporal = temporal.next
                nuevo_nodo = Nodo(data=data, next=temporal.next)
                temporal.next = nuevo_nodo

        self.print_list()
        print("\nPromedio de la lista:", self.calcular_promedio())

    def existente(self, data):
        temporal = self.head
        while temporal:
            if temporal.data == data:
                return True
            temporal = temporal.next
        return False

    def calcular_promedio(self):
        suma = 0
        contador = 0
        temporal = self.head
        while temporal:
            suma = suma + temporal.data
            contador = contador + 1
            temporal = temporal.next
            prom = suma / contador
        return prom
    

# Bloque de código para probar la funcionalidad
if __name__ == "__main__":
    lista = Lista_enlazada()
    lista.insertar_dato(7)
    lista.insertar_dato(-9)
    lista.insertar_dato(0)
    lista.insertar_dato(5)
