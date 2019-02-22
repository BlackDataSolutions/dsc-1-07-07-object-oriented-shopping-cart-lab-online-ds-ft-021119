class ShoppingCart:
    # write your code here
    def __init__(self, employee_discount=None):
        self.total = 0
        self.employee_discount = employee_discount
        self.items = []
     
    
    
    def add_item(self, name, price, quantity=1):
        self.name = name
        self.calculated_price = price * quantity
        self.quantity = quantity
        
        if self.quantity == 1:
            self.items.append({"name": name, "price": price})
        else:
            for item in range(0, self.quantity):
                self.items.append({"name": name, "price": price})
                
        self.total += self.calculated_price
        return self.total

    def show_item_list(self):
        return self.items


    def mean_item_price(self):
        return round(self.total / len(self.items), 3)
    

    def median_item_price(self):
        sorted_list = sorted(self.items, key= lambda cost: cost['price'])
        price_list = [item['price'] for item in sorted_list]
        length = len(price_list)
        if (length % 2 == 0):
            mid_upper = price_list[int(length / 2)]
            mid_lower = price_list[int((length / 2) - 1)]
            median = (mid_upper + mid_lower) / 2
            return round(median, 3)
        else:
            median = price_list[int((length - 1)/2)]
            return median
        

    def apply_discount(self):
        if self.employee_discount:
            discounted_total = (self.total * ( 1 - (self.employee_discount / 100)))
            return discounted_total
        else:
            return "Sorry, there is no discount to apply to your cart :("

    def void_last_item(self):
        if self.items:
            removed_item = self.items.pop()
        else:
            return "There are no items in your cart!"
        self.total -= removed_item['price']