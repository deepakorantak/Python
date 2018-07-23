class ShoppingCart:
    def __init__(self):
        self._list = dict()

    def add_cart(self,order):
        if (order.item in self._list):
            self._list[order.item] += order.qty
        else:
            self._list[order.item] = order.qty
        return (True,"Order processed")

    def delete_cart(self,order):
        if ((order.item in self._list) and (self._list[order.item] > order.qty)):
            self._list[order.item] -= order.qty
        elif ((order.item in self._list) and (self._list[order.item] <= order.qty)):
            del self._list[order.item]
        else:
            return (False,"Item not present")       
        return (True,"Order processed")

    def __repr__(self):
        return " The cart contents: {0}".format(self.__dict__["_list"])

    def __str__(self):
        return " Str The cart contents: {0}".format(self.__dict__["_list"])

class Order:
    def __init__(self,option,item,qty):
        if not option in ["a","d"]:
            raise ValueError("Invalid option entered {}".format(option))
        else:
            self.option = option
        
        try:
            self.qty = int(qty)
        except :
            raise ValueError("Quantity Entered is not numeric {}".format(qty))

        if qty <= 0:
            raise ValueError("Quantity Entered negative or zero {}".format(qty))
        else:
             self.qty = qty
        
        self.item = item
       

def process_order(ord):
    if (ord.option == "a"):
        cart.add_cart(ord)
    elif (ord.option == "d"):
        cart.delete_cart(ord)  
    else:
        return (False,"Invalid option")
    return (True,"Order processed")

def get_order():
    print("Enter your choice : ")
    print("Enter a <item> <qty>: to add to shopping list")
    print("Enter d <item> <qty>: to delete from shopping list")
    print("Enter q: to quit shopping")
    print("")
    user_input = input()
    option = user_input[:1]
    if option == "q":
        item = ""
        qty = ""
    else:
        option,item,qty = user_input.split(" ")       
     
    return Order(option,item,qty)

   
exit_shopping = False
cart = ShoppingCart()

while not exit_shopping:
    o1 = get_order()    
    if o1.option == "q":
        exit_shopping = True
        break
    result = process_order(o1)
    print(result)    
print(cart)
    

    

