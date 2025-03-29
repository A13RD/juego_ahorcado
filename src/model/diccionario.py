import random


class Diccionario:

    def __init__(self):
        """
            Inicializa una instancia de la clase Diccionario, cargando las palabras desde un archivo.

            Attributes:
                palabras (list[str]): Lista de palabras cargadas desde el archivo.

            Methods:
                __cargar_palabras() -> list[str]:
                    Carga las palabras desde el archivo "assets/palabras.txt" y las devuelve en una lista.

                obtener_palabra() -> str:
                    Selecciona y retorna una palabra aleatoria de la lista de palabras disponibles.
        """
        self.palabras: list[str] = self.__cargar_palabras()

    def __cargar_palabras(self) -> list[str]:
       
        palabras = []
        with open("assets/palabras.txt", "r", encoding="utf8") as archivo:
            for line in archivo:
                palabras.append(line.strip())

        return palabras

    def obtener_palabra(self) -> str:
        indice_aleatorio = random.randint(0, len(self.palabras) - 1)
        return self.palabras[indice_aleatorio]
