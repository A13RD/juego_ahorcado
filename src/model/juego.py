from src.model.diccionario import Diccionario
from src.model.adivinanza import Adivinanza
from src.model.error_intentos_insuficientes import ErrorIntentosInsuficientes


class Juego:

    """
    Representa la lógica del juego del ahorcado, gestionando la dificultad, los intentos y la palabra a adivinar.

    Attributes:
        DIFICULTAD_BAJA (str): Constante para la dificultad baja.
        DIFICULTAD_MEDIA (str): Constante para la dificultad media.
        DIFICULTAD_ALTA (str): Constante para la dificultad alta.
        __dificultad (str): Nivel de dificultad actual del juego.
        __intentos_realizados (int): Número de intentos restantes para adivinar la palabra.
        __diccionario (Diccionario): Instancia del diccionario para obtener palabras aleatorias.
        __adivinanza (Adivinanza | None): Instancia de la palabra a adivinar en la partida.

    Methods:
        obtener_intentos_realizados() -> int:
            Retorna la cantidad de intentos restantes.

        obtener_adivinanza() -> Adivinanza:
            Devuelve la instancia de la palabra a adivinar.

        __generar_palabra() -> str:
            Obtiene una palabra aleatoria del diccionario.

        calcular_intentos_permitidos() -> int:
            Calcula y retorna la cantidad de intentos permitidos según la dificultad.

        modificar_dificultad(dificultad: str) -> None:
            Modifica el nivel de dificultad del juego.

        iniciar_partida() -> int:
            Inicia una nueva partida, generando una palabra y estableciendo los intentos disponibles.
            Retorna la cantidad de caracteres de la palabra.

        adivinar(letra: str) -> list[int]:
            Intenta adivinar una letra de la palabra.
            
            Args:
                letra (str): Letra que el jugador quiere adivinar.

            Returns:
                list[int]: Lista con las posiciones donde aparece la letra en la palabra. Vacía si la letra no está.

            Raises:
                ErrorIntentosInsuficientes: Si no quedan intentos disponibles.

        verificar_si_hay_intentos() -> bool:
            Verifica si quedan intentos disponibles.

        verificar_triunfo() -> bool:
            Verifica si todas las letras de la palabra han sido adivinadas.
    """

    DIFICULTAD_BAJA = "DIFICULTAD_BAJA"
    DIFICULTAD_MEDIA = "DIFICULTAD_MEDIA"
    DIFICULTAD_ALTA = "DIFICULTAD_ALTA"

    def __init__(self):
        self.__dificultad = Juego.DIFICULTAD_BAJA
        self.__intentos_realizados: int = 0
        self.__diccionario = Diccionario()
        self.__adivinanza: Adivinanza = None

    def obtener_intentos_realizados(self):
        return self.__intentos_realizados

    def obtener_adivinanza(self) -> Adivinanza:
        return self.__adivinanza

    def __generar_palabra(self) -> str:
        return self.__diccionario.obtener_palabra()

    def calcular_intentos_permitidos(self) -> int:
        if self.__dificultad == self.DIFICULTAD_BAJA:
            return 20
        if self.__dificultad == self.DIFICULTAD_MEDIA:
            return 10
        if self.__dificultad == self.DIFICULTAD_ALTA:
            return 5

        return 0

    def modificar_dificultad(self, dificultad: str) -> None:
        self.__dificultad = dificultad

    def iniciar_partida(self) -> int:
        palabra = self.__generar_palabra()
        self.__adivinanza: Adivinanza = Adivinanza(palabra)
        self.__intentos_realizados = self.calcular_intentos_permitidos()
        return self.__adivinanza.obtener_cantidad_posiciones()

    def adivinar(self, letra: str) -> [int]:
        """
            Intenta adivinar una letra de la palabra.

            Args:
                letra (str): Letra que el jugador quiere adivinar.

            Returns:
                list[int]: Lista con las posiciones donde aparece la letra en la palabra. Vacía si la letra no está.

            Raises:
                ErrorIntentosInsuficientes: Si no quedan intentos disponibles.
        """
        if self.__intentos_realizados < 0:
            raise ErrorIntentosInsuficientes()
        self.__intentos_realizados -= 1
        return self.__adivinanza.adivinar(letra)

    def verificar_si_hay_intentos(self) -> bool:
        return self.__intentos_realizados >= 0

    def verificar_triunfo(self) -> bool:
        return self.__adivinanza.verificar_si_hay_triunfo()