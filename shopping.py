products = {"milk":1.00,"bread":2.79,"salad":2.20,"coke":1.19,"water":2.09}
cart ={}
for key,value in products.items():
    print(key,value)
while True:
    product_name = input("enter: the name of the product that you want to add to the cart.(type 'stop' if you are done.):")
    if product_name == "stop":
        break
    elif product_name not in products:
        print("this product is not available.")
        continue
        
    product_quantity = int(input("enter: the quantity of this product:"))


    cart [product_name] = product_quantity
prod_total = 0 

for key,value in cart.items():
    prod_amount = value * products[key]
    print(key,value,products[key],prod_amount)
    prod_total = prod_total + prod_amount
   
print(prod_total)



