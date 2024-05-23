# Task One -

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0
    
    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Can't dequeue from an empty queue!")
    
    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Can't peek from an empty queue.")
        
    def size(self):
        return len(self.items)
    



    
# Task Two - 

class Menu:
    def __init__(self):
        self.item = Queue()
    
    def add_to_menu(self, menu_item):
        self.item.enqueue(menu_item)
        print(f"{menu_item} has been added!")

    def show_menu(self):
        if not self.item.is_empty():
            menu_item = self.item.dequeue()
            print(f"Your menu item search: {menu_item}")
        else:
            print("There are no menu items.")




# Task Three -

class Order:
    def __init__(self):
        self.order = Queue()



# Task Four -

def add_to_orders(self, customer_order):
    self.order.enqueue(customer_order)
    print(f"Customer Order: {customer_order}")

def show_customer_order(self):
    if not self.order.is_empty():
        customer_order = self.order.dequeue()
        print(f"This customer\'s order: {customer_order}")
    else:
        print("No orders have been placed")






# Task Five - 

food_menu = Menu()
customers = Order()

food_menu.add_to_menu("Spaghetti Carbonara")
food_menu.add_to_menu("Margherita Pizza")
food_menu.add_to_menu("Chicken Alfredo")

food_menu.show_menu()
customers.add_to_orders()
customers.show_customer_order()