from logic.products import findA11
from tabulate import tabulate


def design():
    print("""
        Menu de prodectos 
          1. ver productos
          2. ver procuctos por categoria
          3. Actualizar el inventario de un  producto
          0. salir 
    """)
    return int(input())
#def tableProducts():
#    data = findA11()
#    print("    Todos los productos\n")
#    indice = 0
#    for product in data:
#        print(f'\t {indice}. {product.get("nombre")} | category: {product.get("categoria")} | price:{product.get("precio_venta")}')
#
#        indice += 1

def tableProducts():
    data = findA11()
    dataModify = []
    for dicionario in data: #para poder quitar un apartados que no quiero en este casa deccionario.pop descripcion etc (primero pasarlo na una libreria ) 
        dicionario.pop("descripcion")
        dicionario.pop("proveedor")
        dicionario.pop("precio_proveedor")
        dataModify.append(dicionario)
    print(tabulate(data, headers="keys" , tablefmt="grid" , numalign="center" ,showindex="always"))

def tableProductsBycategory(category):
    data = findA11()
    dataModify = []
    for dicionario in data:
        if(dicionario.get("categoria") == category):
            dicionario.pop("descripcion")
            dicionario.pop("proveedor")
            dicionario.pop("precio_proveedor")
            dataModify.append(dicionario)
    print(tabulate(dataModify, headers="keys" , tablefmt="grid" , numalign="center" ,showindex="always"))