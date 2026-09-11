from estructura_cola import Queue


def invertir_cola(cola):
    if cola.is_empty():
        return

    elemento = cola.dequeue()

    invertir_cola(cola)

    cola.enqueue(elemento)


cola = Queue()

cola.enqueue(10)
cola.enqueue(20)
cola.enqueue(30)
cola.enqueue(40)
cola.enqueue(50)

print("Cola original:", cola.mostrar())

if cola.is_empty():
    print("La cola está vacía")
else:
    invertir_cola(cola)

print("Cola invertida:", cola.mostrar())
