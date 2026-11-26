
# Clase para crear los nodos
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None


# 1. Recorrido Preorden
def Preorden(nodo):
    if nodo is not None:
        print(nodo.valor, end=", ")
        Preorden(nodo.izquierdo)
        Preorden(nodo.derecho)


# 2. Recorrido Inorden
def Inorden(nodo):
    if nodo is not None:
        Inorden(nodo.izquierdo)
        print(nodo.valor, end=", ")
        Inorden(nodo.derecho)


# 3. Recorrido Postorden
def Postorden(nodo):
    if nodo is not None:
        Postorden(nodo.izquierdo)
        Postorden(nodo.derecho)
        print(nodo.valor, end=", ")


# 4. Recorrido por niveles
def PorNiveles(raiz):
    if raiz is None:
        return

    from collections import deque
    cola = deque()
    cola.append(raiz)

    while cola:
        nodo = cola.popleft()
        print(nodo.valor, end=", ")

        if nodo.izquierdo is not None:
            cola.append(nodo.izquierdo)

        if nodo.derecho is not None:
            cola.append(nodo.derecho)


# Crear el árbol
raiz = Nodo(50)
raiz.izquierdo = Nodo(30)
raiz.derecho = Nodo(70)

raiz.izquierdo.izquierdo = Nodo(20)
raiz.izquierdo.derecho = Nodo(40)

raiz.derecho.izquierdo = Nodo(60)
raiz.derecho.derecho = Nodo(80)


# Ejecutar los cuatro recorridos
print("Recorrido Preorden:")
Preorden(raiz)

print("\n\nRecorrido Inorden:")
Inorden(raiz)

print("\n\nRecorrido Postorden:")
Postorden(raiz)

print("\n\nRecorrido Por Niveles:")
PorNiveles(raiz)

print()

