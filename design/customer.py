from logic.products import findAll as findAllProducts, saveAll as saveAllProducts, updateInventoryByCode
from logic.orders import findAll as findAllOrders, addProductByOrder, addOrder
from tabulate import tabulate
from datetime import datetime

def designClient():
    print("""
    Menu de clientes
        0. Salir
        1. Realizar pedido
        2. Ver pedidos realizados
    """)
    opc = int(input())
    return opc

def formularyTakeOrder():
    dataProducts = findAllProducts()
    dataOrders = findAllOrders()
    findProductsMajor = list(filter(lambda product: product.get("cantidad_en_stock") > 0, dataProducts))
    findProducts = list(filter(lambda product: (product.pop("descripcion"), product.pop("proveedor"), product.pop("precio_proveedor")), findProductsMajor))
    print("Lista de productos disponibles:")
    print(tabulate(findProducts, headers= "keys", tablefmt="grid", numalign="center", showindex="always"))
    dataProducts = findAllProducts()
    print(" ")
    print("¿Que desea ordenar?")
    now = datetime.now()
    for indice, product in enumerate(dataOrders):
        dataOrders[indice] = product.get("codigo_pedido")
        #dataOrders = list(dataOrders[-1].get("codigo_pedido"))
    formulary = dict({
        "codigo_pedido": dataOrders[-1] + 1,
        "codigo_cliente": f"CL-{dataOrders[-1] + 1}",
        "fecha_pedido": now.strftime('%Y-%m-%d'),
        "detalles_pedido": list(),
    })
    formulary = addProductByOrder(formulary, findProductsMajor)
    responseProducts = updateInventoryByCode(formulary.get("detalles_pedido"))
    print(responseProducts)
    responseOrders = addOrder(formulary)
    print(responseOrders)

def tableOrders():
    dataOrders = findAllOrders()
    dataModify = []
    for diccionario in dataOrders:
        diccionario.pop("codigo_pedido")
        dataModify.append(diccionario)
    print(tabulate(dataModify, headers= "keys", tablefmt="grid"))