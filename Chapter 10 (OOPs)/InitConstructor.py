class Grocery:
    vegetable = "Potato"
    price = 50
    weight = "1kg"

    # Init method will automatically be called whenever the object of the class will be created!    

    def __init__(self, extra):     # This is a constructor! Init is a dunder method which starts with __ ! 
        print("This is a class representing Grocery items!")
        Grocery.extraItem = extra


ForChokha = Grocery("Onion")
print(Grocery.vegetable, Grocery.price, Grocery.extraItem)