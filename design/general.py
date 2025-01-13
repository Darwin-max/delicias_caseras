from design.products import desing as designProducts, tableProducts, tableProductsByCategory, tableProductsByCode, tableProductsByName
from design.general import *
from logic.products import updateInventoryByCode, addNewProduct
from design.customer import *
from design.orders import designOrder, actualizar_detalles_pedido
from logic.orders import *

def menu():
    print("""
          **
                                Bienvenido al menú principal
             Registrar pedidos   |   Productos   |   Editar pedidos   |   Salir
                     1           |       2       |         3          |     0
          **
          """)
principal = input("Ingrese el número de la opción: ")
match principal:
        case "1":
           while True:
               option = designClient()
               match option:
                    case "1":
                       formularyTakeOrder()
                    case "2":
                       tableOrders()
                    case "0":
                        break
        case "2":   
            while True:
                option = designProducts()
                match option:
                    case 1:
                        tableProducts()
                    case 2:
                        tableProductsByCategory(input("Ingrese la categoria. Ejemplo ('pan', 'pastel', 'postre'): ").lower())
                    case 3:
                        tableProductsByCode(input("Ingrese el codigo del producto: "))
                    case 4:
                        tableProductsByName(input("Ingrese el nombre del producto: "))
                    case 5:
                        updateInventoryByCode(input("Ingrese el codigo del producto: "))
                    case 6:
                        addNewProduct() 
                    case 0:
                        break
        # case "3":
        #     while True:
        #         option = designOrder()
        #         match option:
                   
        #             case 1:
        #                actualizar_detalles_pedido(int(input("Ingrese el codigo del pedido: ")))
        #             case 2:
        #                 deleteJSON(int(input("Ingrese el codigo del pedido: ")))
        #             case 0:
        #               break
        case "0":
            print("Gracias por utilizar nuestro sistema")
            
        case _:
            print("Opción no válida")
        