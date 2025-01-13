from logic.products import *
from tabulate import tabulate

def desing():
    print("""
    Menu de productos
        0. Salir
        1. Ver productos
        2. Ver producto por categoria
        3. Ver producto por nombre
        4. Ver producto por codigo
        5. Actualizar el inventario de un producto
        6. Agregar un nuevo producto
    """)
    opc = int(input())
    return opc

def tableProducts():
    data = findAll()
    dataModify = []
    for diccionario in data:
        diccionario.pop("descripcion")
        diccionario.pop("proveedor")
        diccionario.pop("precio_proveedor")
        dataModify.append(diccionario)
    print(tabulate(dataModify, headers= "keys", tablefmt="grid", numalign="center", showindex="always"))

def formularyAddProduct():
    data = findAll()
    codeProduct = input("Codigo: ")
    findProducts = list(filter(lambda product: product.get("codigo_producto") == codeProduct, data))
    if(not len(findProducts)):
        formulary = dict({
            "codigo_producto": codeProduct,
            "nombre": input("Nombre: "),
            "cateogria": input("Categoria, ejemplo (Panes, Pastel, Postres: "),
            "descripcion": input("Descripcion breve: : "),
            "cantidad_en_stock": 0,
            "precio_venta": input("Precio de venta: : "),
            "precio_proveedor": input("Precio de compra: ")
        })
        response = add_product(formulary)
        print(response)
    else:
        print("El producto ya existe")

def tableProductsByCategory():
    Category = input("Ingrese la categoria a buscar, ejemplo (Panes, Pastel, Postres): ").capitalize()
    data = findAll()
    dataModify = []
    for diccionario in data:
        if (diccionario.get("categoria") == Category):
            diccionario.pop("descripcion")
            diccionario.pop("proveedor")
            diccionario.pop("precio_proveedor")
            dataModify.append(diccionario)
    print(tabulate(dataModify, headers= "keys", tablefmt="grid", numalign="center", showindex="always"))

def tableProductsByName():
    name = input("Ingrese el nombre del producto, ejemplo (Pan Integral): ").capitalize()
    data = findAll()
    dataModify = []
    for diccionario in data:
        if (diccionario.get("nombre") == name):
            diccionario.pop("descripcion")
            diccionario.pop("proveedor")
            diccionario.pop("precio_proveedor")
            dataModify.append(diccionario)
    print(tabulate(dataModify, headers= "keys", tablefmt="grid", numalign="center", showindex="always"))

def tableProductsByCode():
    code = input("Ingrese el codigo de producto, ejemplo (PN-001): ").upper()
    data = findAll()
    dataModify = []
    for diccionario in data:
        if (diccionario.get("codigo_producto") == code):
            diccionario.pop("descripcion")
            diccionario.pop("proveedor")
            diccionario.pop("precio_proveedor")
            dataModify.append(diccionario)
    print(tabulate(dataModify, headers= "keys", tablefmt="grid", numalign="center", showindex="always"))