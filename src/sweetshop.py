class SweetShop:
    def __init__(self):
        self.sweets = []

    def add_sweet(self, sweet):
        self.sweets.append(sweet)
    def delete_sweet(self, sweet_id):
        self.sweets = [sweet for sweet in self.sweets if sweet.id != sweet_id]
    def view_sweets(self):
        return self.sweets