from queue_structure import Queue


cola = Queue()

cola.enqueue(10)
cola.enqueue(50)
cola.enqueue(20)
cola.enqueue(30)
cola.enqueue(40)

print("Cola original:", cola.mostrar())

elementos = cola.mostrar()
mayor = max(elementos)

elementos.remove(mayor)

cola.vaciar()

for elemento in elementos:
    cola.enqueue(elemento)

cola.enqueue(mayor)

print("Número mayor:", mayor)
print("Cola después:", cola.mostrar())