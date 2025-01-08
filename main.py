from design.products import design, tableProducts


match design():
    case 1 : 
        tableProducts()
  
    case _:
        print("Esa obcion no existe")