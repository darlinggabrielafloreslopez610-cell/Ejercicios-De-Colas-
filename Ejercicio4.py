from queue_structure import Queue


cola = Queue()

cola.enqueue(30)
cola.enqueue(10)
cola.enqueue(50)
cola.enqueue(20)
cola.enqueue(40)

print("Cola original:", cola.mostrar())

elementos = cola.mostrar()
menor = min(elementos)

elementos.remove(menor)

cola.vaciar()

for elemento in elementos:
    cola.enqueue(elemento)

cola.colocar_al_frente(menor)

print("Número menor:", menor)
print("Cola después:",
cola.mostrar())