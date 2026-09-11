from estructura_cola import Queue


def eliminar_ceros(cola):
    cola_sin_ceros = Queue()
    temporal = Queue()

    if cola.is_empty():
        return cola_sin_ceros

    while not cola.is_empty():
        elemento = cola.dequeue()

        if elemento != 0:
            cola_sin_ceros.enqueue(elemento)

        temporal.enqueue(elemento)

    while not temporal.is_empty():
        cola.enqueue(temporal.dequeue())

    return cola_sin_ceros


cola = Queue()

cola.enqueue(5)
cola.enqueue(0)
cola.enqueue(8)
cola.enqueue(0)
cola.enqueue(3)

print("Cola original:", cola.mostrar())

cola_sin_ceros = eliminar_ceros(cola)

print("Cola sin ceros:", cola_sin_ceros.mostrar())
print("Cola original después de la operación:", cola.mostrar())
