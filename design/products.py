from tabulate import tabulate
from logic.products import findall

def design():
    print("""
        Menu de prodectos 
          1. ver productos
          2. ver procuctos por categoria
          3. Actualizar el inventario de un  producto
          4. Agregar nuevo producto
          0. salir 
    """)
    return int(input())


def tableProducts():
    data = findAll()
    dataModify = []
    for dicionario in data: #para poder quitar un apartados que no quiero en este casa deccionario.pop descripcion etc (primero pasarlo na una libreria ) 
        dicionario.pop("descripcion")
        dicionario.pop("proveedor")
        dicionario.pop("precio_proveedor")
        dataModify.append(dicionario)
    print(tabulate(data, headers="keys" , tablefmt="grid" , numalign="center" ,showindex="always"))

def tableProductsBycategory(category):
    data = findall()
    dataModify = []
    for dicionario in data:
        if(dicionario.get("categoria") == category):
            dicionario.pop("descripcion")
            dicionario.pop("proveedor")
            dicionario.pop("precio_proveedor")
            dataModify.append(dicionario)
    print(tabulate(dataModify, headers="keys" , tablefmt="grid" , numalign="center" ,showindex="always"))



   