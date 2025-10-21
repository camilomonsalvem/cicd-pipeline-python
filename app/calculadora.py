"""
Módulo de funciones matemáticas básicas para la calculadora.
Incluye operaciones de suma, resta, multiplicación y división.
"""


def sumar(a, b):
    """
    Suma dos números.

    Args:
        a (float | int): Primer número.
        b (float | int): Segundo número.

    Returns:
        float | int: Resultado de la suma.
    """
    return a + b


def restar(a, b):
    """
    Resta dos números.

    Args:
        a (float | int): Minuendo.
        b (float | int): Sustraendo.

    Returns:
        float | int: Resultado de la resta.
    """
    return a - b


def multiplicar(a, b):
    """
    Multiplica dos números.

    Args:
        a (float | int): Primer número.
        b (float | int): Segundo número.

    Returns:
        float | int: Producto de los números.
    """
    return a * b


def dividir(a, b):
    """
    Divide dos números.

    Args:
        a (float | int): Dividendo.
        b (float | int): Divisor (no puede ser cero).

    Raises:
        ZeroDivisionError: Si el divisor es cero.

    Returns:
        float: Resultado de la división.
    """
    if b == 0:
        raise ZeroDivisionError("No se puede dividir por cero")
    return a / b


def potencia(a, b):
    """
    Calcula la potencia de un número elevado a otro.

    Args:
        a (float | int): Base.
        b (float | int): Exponente.

    Returns:
        float | int: Resultado de elevar a a la potencia b.
    """
    return a**b


def modulo(a, b):
    """
    Calcula el residuo de la división entre dos números.

    Args:
        a (float | int): Dividendo.
        b (float | int): Divisor (no puede ser cero).

    Raises:
        ZeroDivisionError: Si el divisor es cero.

    Returns:
        float | int: Residuo de la división de a entre b.
    """
    if b == 0:
        raise ZeroDivisionError("No se puede calcular el módulo con divisor cero")
    return a % b
