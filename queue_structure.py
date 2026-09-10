class Cola:
    """Clase Queue basada en la Unidad 5."""
    def __init__(self):
        self.items = []

    def is_empty(self) -> bool:
        return len(self.items) == 0

    def enqueue(self, item):
        """Añade un elemento al final (rear) de la cola."""
        self.items.append(item)

    def dequeue(self):
        """Elimina y retorna el elemento del frente (front) de la cola."""
        if not self.is_empty():
            return self.items.pop(0)
        raise IndexError("La cola está vacía")

    def front(self):
        """Retorna el elemento del frente sin eliminarlo."""
        if not self.is_empty():
            return self.items[0]
        raise IndexError("La cola está vacía")

    def size(self) -> int:
        """Retorna la cantidad de elementos en la cola."""
        return len(self.items)