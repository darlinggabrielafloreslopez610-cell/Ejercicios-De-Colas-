from queue_structure import Queue


cola = Queue()

cola.enqueue(10)
cola.enqueue(20)
cola.enqueue(30)
cola.enqueue(40)
cola.enqueue(50)

print("Cola:", cola.mostrar())

print("Cantidad de elementos:", cola.size())