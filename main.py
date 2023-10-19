class Order:
    def __init__(self, order_number, order_date, ship_to, ship_from):
        self.order_number = order_number
        self.order_date = order_date
        self.ship_to = ship_to
        self.ship_from = ship_from
        self.order_status = "Pending" # Default status

    def change_order_status(self, new_status):
        self.order_status = new_status

    def view_details(self):
        print("Order Number: ", self.order_number)
        print("Order Date: ", self.order_date)
        print("Ship To: ", self.ship_to)
        print("Ship From: ", self.ship_from)
        print("Order Status: ", self.order_status)

# Example usage:
order1 = Order("12345", "2023-10-19", "123 Main St, City", "456 Park Ave, Town")
order1.view_details()
order1.change_order_status("Shipped")
order1.view_details()
