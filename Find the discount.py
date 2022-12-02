
def dis(price_def, pourcentage_def):
    return (price_def / 100) * pourcentage_def


price = 36
pourcentage = 50
real_price = dis(price, pourcentage)
print(real_price)
