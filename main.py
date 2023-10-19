#push dito
class seller:
    def __init__(self, seller_ID, Phone_number, Address):
        self._seller_ID = seller_ID
        self._Phone_number = Phone_number
        self.Address = Address

    def get_seller_ID(self):
        return self._seller_ID
    def get_Phone_number(self):
        return self._Phone_number
    def get_Address(self):
        return self.Address

seller = seller("124343", "092134342", "Palawan")
print("Seller ID: ", seller.get_seller_ID())
print("Phone number: ", seller.get_Phone_number())
print("Address: ", seller.get_Address())
