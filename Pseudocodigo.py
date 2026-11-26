
# Clase para crear los nodos
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None


# 1. Recorrido Preorden
def Preorden(nodo):
    if nodo is not None:
        print(nodo.valor, end=" ")
        Preorden(nodo.izquierdo)
        Preorden(nodo.derecho)


# 2. Recorrido Inorden
def Inorden(nodo):
    if nodo is not None:
        Inorden(nodo.izquierdo)
        print(nodo.valor, end=" ")
        Inorden(nodo.derecho)


# 3. Recorrido Postorden
def Postorden(nodo):
    if nodo is not None:
        Postorden(nodo.izquierdo)
        Postorden(nodo.derecho)
        print(nodo.valor, end=" ")


# 4. Recorrido por niveles
def PorNiveles(raiz):
    if raiz is None:
        return

    from collections import deque
    cola = deque([raiz])

    while cola:
        nodo = cola.popleft()
        print(nodo.valor, end=" ")

        if nodo.izquierdo is not None:
            cola.append(nodo.izquierdo)

        if nodo.derecho is not None:
            cola.append(nodo.derecho)


# 5. Buscar un elemento
def Buscar(nodo, valor):
    if nodo is None:
        return False

    if nodo.valor == valor:
        return True

    if valor < nodo.valor:
        return Buscar(nodo.izquierdo, valor)

    return Buscar(nodo.derecho, valor)


# 6. Encontrar el menor valor
def EncontrarMinimo(nodo):
    actual = nodo

    while actual.izquierdo is not None:
        actual = actual.izquierdo

    return actual


# 7. Eliminar un elemento
def Eliminar(nodo, valor):
    if nodo is None:
        return None

    if valor < nodo.valor:
        nodo.izquierdo = Eliminar(nodo.izquierdo, valor)

    elif valor > nodo.valor:
        nodo.derecho = Eliminar(nodo.derecho, valor)

    else:
        # Caso 1: no tiene hijos
        if nodo.izquierdo is None and nodo.derecho is None:
            return None

        # Caso 2: tiene un solo hijo
        elif nodo.izquierdo is None:
            return nodo.derecho

        elif nodo.derecho is None:
            return nodo.izquierdo

        # Caso 3: tiene dos hijos
        sucesor = EncontrarMinimo(nodo.derecho)
        nodo.valor = sucesor.valor
        nodo.derecho = Eliminar(nodo.derecho, sucesor.valor)

    return nodo


# Crear el árbol
raiz = Nodo(50)
raiz.izquierdo = Nodo(30)
raiz.derecho = Nodo(70)

raiz.izquierdo.izquierdo = Nodo(20)
raiz.izquierdo.derecho = Nodo(40)

raiz.derecho.izquierdo = Nodo(60)
raiz.derecho.derecho = Nodo(80)


# Mostrar los recorridos
print("Preorden:")
Preorden(raiz)

print("\n\nInorden:")
Inorden(raiz)

print("\n\nPostorden:")
Postorden(raiz)

print("\n\nPor niveles:")
PorNiveles(raiz)


# Buscar elementos
print("\n\nBuscar 60:", Buscar(raiz, 60))
print("Buscar 90:", Buscar(raiz, 90))


# Eliminar el nodo 20
raiz = Eliminar(raiz, 20)

# Mostrar el árbol después de eliminar
print("\n\nInorden despues de eliminar 20:")
Inorden(raiz)

print()


