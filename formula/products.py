def  updateQuantityInventory(stok, quantity):
    if(quantity > 0):
        stok = stok + quantity
        return stok
    else:
        return stok