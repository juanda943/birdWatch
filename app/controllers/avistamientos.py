
from collections import deque
from datetime import datetime

avistamientos = []
ultimos_avistamientos = deque(maxlen=10)

class NodoEspecie:
    def __init__(self, especie):
        self.especie = especie
        self.registros = []
        self.izquierda = None
        self.derecha = None

    def insertar(self, especie, datos):
        if especie == self.especie:
            self.registros.append(datos)
        elif especie < self.especie:
            if self.izquierda is None:
                self.izquierda = NodoEspecie(especie)
            self.izquierda.insertar(especie, datos)
        else:
            if self.derecha is None:
                self.derecha = NodoEspecie(especie)
            self.derecha.insertar(especie, datos)

    def en_orden(self):
        result = []
        if self.izquierda:
            result.extend(self.izquierda.en_orden())
        result.append((self.especie, self.registros))
        if self.derecha:
            result.extend(self.derecha.en_orden())
        return result

arbol_especies = None

def ordenar_por_fecha(data):
    return sorted(data, key=lambda x: datetime.strptime(x["fecha"], "%Y-%m-%d"))

def ordenar_por_lugar(data):
    return sorted(data, key=lambda x: x["ubicacion"])
