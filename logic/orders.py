from logic.products import findAll as findAllProducts, saveAll as saveAllProducts
import json

def findAll():
    with open("data/order.json", "r", encoding="utf-8") as file :
        dataOrders = file.read()
        convertedList = json.loads(dataOrders)
        return convertedList

def savell(dataOrders):
    with open("data/order.json", "w", encoding="utf-8") as file:
        str(dataOrders).encode('utf-8')
        convertJSON = json.dumps(dataOrders, indent=4, ensure_ascii=False)
        file.write(convertJSON)
        return "Se modifico el archivo orders.json"

def addOrder(formulary):
    dataOrders = findAll()
    dataOrders.append(formulary)
    return savell(dataOrders)

def addProductByOrder(formulary, listProducts):
    while True:
        codigo_producto = input("Ingrese el codigo de producto, ejemplo (PN-001): ")
        select = list(filter(lambda product: product.get("codigo_producto") == codigo_producto, listProducts))
        if(len(select) != 0 and input("¿Desea agregar este producto a su pedido? (S/N): ").upper() == "S"):
            cantidad = int(input("Ingrese la cantidad de producto que desea pedir: "))
            if(cantidad <= select[0].get("cantidad_en_stock")):
                formulary["detalles_pedido"].append({
                    "codigo_producto": codigo_producto,
                    "cantidad": cantidad,
                    "precio_unidad": select[0].get("precio_venta"),
                    "numero_linea": 1
                })
                if(input("¿Desea agregar mas productos? (S/N): ").upper() == "N"): break
            else:
                print("No hay suficiente en stock")
        else:
            print("Prodcut dataProducts = findAllProducts()o no encontrado")
    return formulary





