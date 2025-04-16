"""Este módulo contiene clases para representar figuras geométricas como 
rectángulos, triángulos y círculos, con la capacidad de calcular sus áreas."""

from abc import ABC, abstractmethod

class FiguraGeometrica(ABC):
    """Clase abstracta para definir la interfaz de figuras geométricas."""

    @abstractmethod
    def calcular_area(self):
        """Método abstracto para calcular el área de una figura."""

    @abstractmethod
    def get_dimensiones(self):
        """Método abstracto para obtener las dimensiones de la figura."""


class Rectangulo(FiguraGeometrica):
    """Clase que representa un rectángulo."""

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        """Calcula el área del rectángulo."""
        return self.base * self.altura

    def __str__(self):
        """Devuelve una representación en cadena del rectángulo."""
        return f"Rectángulo de base {self.base} y altura {self.altura}"

    def get_dimensiones(self):
        """Devuelve las dimensiones del rectángulo."""
        return f"Base: {self.base}, Altura: {self.altura}"


class Triangulo(FiguraGeometrica):
    """Clase que representa un triángulo."""

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        """Calcula el área del triángulo."""
        return (self.base * self.altura) / 2

    def __str__(self):
        """Devuelve una representación en cadena del triángulo."""
        return f"Triángulo de base {self.base} y altura {self.altura}"

    def get_dimensiones(self):
        """Devuelve las dimensiones del triángulo."""
        return f"Base: {self.base}, Altura: {self.altura}"


class Circulo(FiguraGeometrica):
    """Clase que representa un círculo."""

    def __init__(self, radio):
        self.pi = 3.14159
        self.radio = radio

    def calcular_area(self):
        """Calcula el área del círculo."""
        return self.pi * (self.radio ** 2)

    def __str__(self):
        """Devuelve una representación en cadena del círculo."""
        return f"Círculo de radio {self.radio}"

    def get_dimensiones(self):
        """Devuelve las dimensiones del círculo."""
        return f"Radio: {self.radio}"


# Variables globales
BASE_RECTANGULO = 10
ALTURA_RECTANGULO = 5
BASE_TRIANGULO = 7
ALTURA_TRIANGULO = 4
RADIO_CIRCULO = 3

# Ejecución principal
if __name__ == "__main__":
    # Crear instancias de las figuras
    rectangulo = Rectangulo(BASE_RECTANGULO, ALTURA_RECTANGULO)
    triangulo = Triangulo(BASE_TRIANGULO, ALTURA_TRIANGULO)
    circulo = Circulo(RADIO_CIRCULO)

    # Calcular áreas
    print(f"El área del rectángulo es: {rectangulo.calcular_area()}")
    print(f"El área del triángulo es: {triangulo.calcular_area()}")
    print(f"El área del círculo es: {circulo.calcular_area()}")

    # Mostrar representaciones en cadena
    print(rectangulo)
    print(triangulo)
    print(circulo)

    # Mostrar dimensiones de las figurass
    print(rectangulo.get_dimensiones())
    print(triangulo.get_dimensiones())
    print(circulo.get_dimensiones())
