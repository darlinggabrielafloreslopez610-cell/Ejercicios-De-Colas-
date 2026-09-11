from queue_structure import Queue

cola = Queue()

cola.enqueue(10)
cola.enqueue(20)
cola.enqueue(30)
cola.enqueue(40)

print("Cola original:", cola.mostrar())

print("Primer elemento:", cola.front())

print("Cola después:", cola.mostrar())