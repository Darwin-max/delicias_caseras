from formula.products import updateQuantityInventory
from tabulate import tabulate
import json


def findAll():
    with open("data/products.json", "r", encoding="utf-8") as file :
        data = file.read()
        converted = json.loads(data)
        return converted
def saveAll(data):
    with open("data/products.json", "w", encoding="utf-8") as file:
        str(data).encode('utf-8')
        convertJSON = json.dumps(data, indent=4, ensure_ascii=False)
        file.write(convertJSON)
        return "Se modifico el archivo products.json"
    
def add_product(data, new_product):
  """Agrega un nuevo producto al objeto JSON."""

  data.append(new_product)
  return data
        
def updateInventoryByCode(code_product):
    data = findAll()
    for product in data:
        if(product.get('codigo_producto') == code_product):
            quantity = int(input("Ingrese la cantidad de productos que desea actualizar: "))
            stock = updateQuantityInventory(product.get("cantidad_en_stock"), quantity)
            product.update({"cantidad_en_stock": stock})
            print(F"Se actualizo el stock de {code_product} a {stock}")
        #else: print("El codigo de ese producto no existe en este inventario.")
    print(saveAll(data))
    #print(tabulate(data, headers="keys", tablefmt="grid", numalign="center", showindex="always"))
def addNewProduct():
 
  new_product = {}
  new_product["codigo_producto"] = input("Ingrese el código del producto: ")
  new_product["nombre"] = input("Ingrese el nombre del producto: ")
  new_product["categoria"] = input("Ingrese la categoría del producto: ")
  new_product["descripcion"] = input("Ingrese la descripción del producto: ")
  new_product["proveedor"] = input("Ingrese el proveedor del producto: ")
  new_product["cantidad_en_stock"] = int(input("Ingrese la cantidad en stock: "))
  new_product["precio_venta"] = float(input("Ingrese el precio de venta: "))
  new_product["precio_proveedor"] = float(input("Ingrese el precio del proveedor: "))
  
  # Obtener los datos existentes del JSON
  data = findAll()

  # Agregar el nuevo producto al JSON
  data = add_product(data, new_product)

  # Guardar los cambios en el archivo
  saveAll(data)

  return "Producto agregado exitosamente"