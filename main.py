from design.products import desing as desingProducts, tableProducts, tableProductsByCategory, tableProductsByName, tableProductsByCode, formularyAddProduct
from logic.products import updateInventoryByCode
from  design.customer import designClient as desingCustomer, formularyTakeOrder, tableOrders

match desingCustomer():
    case 0:
        print("¡Hasta luego!")
    case 1:
        formularyTakeOrder()
    case 2:
        tableOrders()
    case _:
        print("Esa opcion no existe")