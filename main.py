from design.products import design, tableProducts, tableProductsBycategory
from logic.products import  updateInventoryByCode

match design():
    case 1 : 
        tableProducts()
    case 2 : 
        tableProductsBycategory(input("Ingrese la categoria ejemplo (panes, pàstel o postres)"))
    case 3 :
        updateInventoryByCode(input("Ingrese el codigo de producto ejemplo (PN-001): "))
    case _:
        print("Esa obcion no existe")
