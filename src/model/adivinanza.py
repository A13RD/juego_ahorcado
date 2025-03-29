class Adivinanza:
    """
        Representa una palabra a adivinar en el juego del ahorcado.

        Attributes:
            __letras (list[str]): Lista de caracteres que conforman la palabra a adivinar.
            __posiciones (list[bool]): Lista de booleanos que indican si cada letra ha sido adivinada.
        
        Methods:
        
        adivinar(letra: str) -> list[int]:
            Intenta adivinar una letra en la palabra. Retorna una lista con las posiciones en las que aparece la letra. Si la letra no está en la palabra, retorna una lista vacía.

        obtener_letras() -> list[str]:
            Devuelve la lista de caracteres que conforman la palabra.

        obtener_posiciones() -> list[bool]:
            Retorna una lista de booleanos indicando qué letras han sido adivinadas.

        obtener_cantidad_posiciones() -> int:
            Devuelve la cantidad de caracteres en la palabra.

        verificar_si_hay_triunfo() -> bool:
            Retorna True si todas las letras han sido adivinadas, False en caso contrario.
    """

    def __init__(self, palabra: str):
        self.__letras: list[str] = list(palabra)
        self.__posiciones: list[bool] = [False] * len(self.__letras)

    def adivinar(self, letra: str) -> [int]:
        if letra not in self.__letras:
            return []

        posiciones_donde_esta_la_letra = []
        for i in range(len(self.__letras)):
            if self.__letras[i] == letra:
                posiciones_donde_esta_la_letra.append(i)
                self.__posiciones[i] = True
        return posiciones_donde_esta_la_letra

    def obtener_letras(self) -> [str]:
        return self.__letras

    def obtener_posiciones(self) -> [bool]:
        return self.__posiciones

    def obtener_cantidad_posiciones(self) -> int:
        return len(self.__letras)

    def verificar_si_hay_triunfo(self) -> bool:
        return all(self.__posiciones)
