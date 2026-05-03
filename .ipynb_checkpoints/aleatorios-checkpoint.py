class Aleat():
    """
    Clase generador de números "aleatorios" usando el algoritmo LGC.

    Implementa un iterador que produce números en el rango [0, m) aplicando
    la fórmula: x_{n+1} = (a * x_n + c) mod m

    Atributos:
        m (int): Módulo de la secuencia (por defecto 2**48, estándar POSIX).
        a (int): Multiplicador (por defecto 25214903917, estándar POSIX).
        c (int): Incremento (por defecto 11, estándar POSIX).
        x (int): Valor actual de la secuencia (semilla inicial x0=1212121).

    Métodos:
        __next__(): Devuelve el siguiente número pseudoaleatorio.
        __iter__(): Devuelve el propio iterador.
        __call__(semilla): Reinicia la secuencia con la semilla indicada.

    >>> rand = Aleat(m=32, a=9, c=13, x0=11)
    >>> for _ in range(4):
    ...     print(next(rand))
    ...
    16
    29
    18
    15

    >>> rand(29)
    >>> for _ in range(4):
    ...     print(next(rand))
    ...
    18
    15
    20
    1
    """

 
    def __init__(self, *, m=2**48, a=25214903917, c=11, x0=1212121):
        self.m = m
        self.a = a
        self.c = c
        self.x = x0
        
    def __next__(self):
        self.x = (self.a * self.x + self.c) % self.m
        return self.x

    def __iter__(self):
        return self

    def __call__(self, semilla):
        self.x = semilla


    
def aleat(*, m=2**48, a=25214903917, c=11, x0=1212121):
    """
    Función generadora de números "aleatorios" usando el algoritmo LGC.

    Genera números en el rango [0, m) aplicando la fórmula:
    x_{n+1} = (a * x_n + c) mod m

    Si se envía un valor mediante send(), la secuencia se reinicia usando
    ese valor como nueva semilla.

    Argumentos (solo por clave):
        m  (int): Módulo (por defecto 2**48, estándar POSIX).
        a  (int): Multiplicador (por defecto 25214903917, estándar POSIX).
        c  (int): Incremento (por defecto 11, estándar POSIX).
        x0 (int): Semilla inicial (por defecto 1212121).

    Salida:
        Genera enteros en [0, m).

    >>> rand = aleat(m=64, a=5, c=46, x0=36)
    >>> for _ in range(4):
    ...     print(next(rand))
    ...
    34
    24
    38
    44

    >>> rand.send(24)
    38
    >>> for _ in range(4):
    ...     print(next(rand))
    ...
    44
    10
    32
    14
    """
    x = x0
    semilla = 0
    while True:
        x = (a * x + c) % m
        semilla = yield x
        if semilla : x = semilla

import doctest
doctest.testmod(verbose=True)