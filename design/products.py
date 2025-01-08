from logic.products import findA11

def design():
    print("""
        Menu de prodectos 
          1. ver productos
          2. salir 
    """)
    return int(input())
def tableProducts():
    data = findA11()
    print("    Todos los productos\n")
    indice = 0
    for product in data:
        print(f'\t {indice}. {product.get("nombre")} | category: {product.get("categoria")} | price:{product.get("precio_venta")}')

        indice += 1