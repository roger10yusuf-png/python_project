class Product():
    def __init__(self,name,id,price,quantity):
        self.name = name
        self.id = id
        self.price = price
        self.quantity = quantity

    def display(self):
        print(self.name, self.id, self.price, self.quantity)

    def check_in_stock(self,number_of_products):
        if self.quantity >= number_of_products:
            print("This product is available.")
        elif self.quantity < number_of_products:
            print("The requested amount of this product is unavailable. There are",self.quantity,"available.")
        elif self.quantity == 0:
            print("This product is out of stock.")

    def product_amount(self,number_of_products):
        result_p_a = self.price * number_of_products
        print("Due to the amount of products you have selected, the total cost will be, " +str(result_p_a))

product1 = Product("shoes",162,50.00,10)
product1.display()
product1.check_in_stock(3)
product1.product_amount(3)

        

    