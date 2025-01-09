from formula.products import updateQuantityInventory
from tabulate import tabulate
import json
def findA11():
    with open("data/products.json" , "r" , encoding="utf-8") as file:
        data = file.read()
        convertlistOrDict = json.loads(data)
        return convertlistOrDict
def saveA11(data):
    with open("data/products.json" , "w" , encoding="utf-8") as file:
        str(data).encode('utf-8')
        convertJSON= json.dumps(data, indent=4, ensure_ascii=False )
        file.write(convertJSON)
        return "se modifico el archivo procts.json"

def updateInventoryByCode(code_product):
    data = findA11()
    for  product in data:
        if(product.get("codigo_product") == code_product):
            quantity = int(input("Ingrese la cantidad delk prodecto que desea actualizar: "))
            stock = updateQuantityInventory(print.get("cantidad_en _estock"), quantity)
            product.update({"catidad_en_stock": stock})
            print(f"Se actualizado el stok de {code_product} a {stock}")
    print(saveAll(data))

   # print(tabulate(data, headers="keys" , tablesefmt="grid", numalign="center", showindex="always"))