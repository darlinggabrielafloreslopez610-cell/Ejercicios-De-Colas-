from estructura_cola import Queue
import math


def crear_cola_raices(cola):
    temporal = Queue()
    raices = Queue()

    if cola.is_empty():
        return raices

    while not cola.is_empty():
        elemento = cola.dequeue()

        raices.enqueue(math.sqrt(elemento))
        temporal.enqueue(elemento)

    while not temporal.is_empty():
        cola.enqueue(temporal.dequeue())

    return raices


cola = Queue()

cola.enqueue(4)
cola.enqueue(9)
cola.enqueue(16)
cola.enqueue(25)

print("Cola original:", cola.mostrar())

cola_raices = crear_cola_raices(cola)

print("Cola con raíces cuadradas:", cola_raices.mostrar())
print("Cola original después de la operación:", cola.mostrar())
