class SweetShop:
    def __init__(self):
        self.sweets = []

    def add_sweet(self, sweet):
        self.sweets.append(sweet)
    def delete_sweet(self, sweet_id):
        self.sweets = [sweet for sweet in self.sweets if sweet.id != sweet_id]
    def view_sweets(self):
        return self.sweets
    def search_by_name(self, name):
        return [sweet for sweet in self.sweets if sweet.name.lower() == name.lower()]
    def search_by_category(self, category):
        return [sweet for sweet in self.sweets if sweet.category.lower() == category.lower()]
    def search_by_price_range(self, min_price, max_price):
        return [sweet for sweet in self.sweets if min_price <= sweet.price <= max_price]
    def purchase_sweet(self, sweet_id, quantity):
        for sweet in self.sweets:
            if sweet.id == sweet_id:
                if sweet.quantity >= quantity:
                    sweet.quantity -= quantity
                    return
                else:
                    raise ValueError("Insufficient stock for purchase")
    def restock_sweet(self, sweet_id, quantity):
        for sweet in self.sweets:
            if sweet.id == sweet_id:
                sweet.quantity += quantity
                return