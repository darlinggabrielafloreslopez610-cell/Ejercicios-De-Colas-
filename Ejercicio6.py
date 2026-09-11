from estructura_cola import Queue


cola = Queue()

cola.enqueue("Carlos")
cola.enqueue("Ana")
cola.enqueue("Pedro")
cola.enqueue("Alberto")
cola.enqueue("Luis")


print("Cola original:", cola.mostrar())


if cola.is_empty():
    print("La cola está vacía")
else:
    encontrado = None
    temporal = Queue()

    while not cola.is_empty():
        elemento = cola.dequeue()

        if encontrado is None and elemento.startswith("A"):
            encontrado = elemento
        else:
            temporal.enqueue(elemento)

    while not temporal.is_empty():
        cola.enqueue(temporal.dequeue())

    if encontrado is not None:
        cola.enqueue(encontrado)
        print("Nombre colocado al fondo:", encontrado)
    else:
        print("No se encontró ningún nombre que inicie con A")


print("Cola final:", cola.mostrar())
