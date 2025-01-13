def deductInventory(stock, resta):
        if(resta > 0):
            stock = stock - resta
            return stock
        else:
            return stock