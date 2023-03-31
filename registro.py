import random


class Articulo:
    def __init__(self, ide, descripcion, precio, lugar, tipo):
        self.ide = ide
        self.descripcion = descripcion
        self.precio = precio
        self.lugar = lugar
        self.tipo = tipo


def to_string(articulo):
    template = "ID: {:<4} | Descripcion: {:<15} | Precio de venta: ${:<7} | Lugar de origen: {:<2} | Tipo: {}"
    return template.format(articulo.ide, articulo.descripcion, articulo.precio, articulo.lugar, articulo.tipo)


def generar_random():
    ide = random.randint(1, 9999)
    descripcion = "Descripcion " + str(random.randint(1, 200))
    precio = round(random.uniform(100, 10000), 2)
    lugar = random.randint(0, 24)
    tipo = random.randint(0, 29)
    articulo = Articulo(ide, descripcion, precio, lugar, tipo)
    return articulo


if __name__ == '__main__':
    x = generar_random()
    print(to_string(x))
