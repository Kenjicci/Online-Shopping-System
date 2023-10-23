class Admin(User):
    def __init__(self, username, user_id, password):
        super().__init__(username, user_id, password)

    def display_seller_info(self):
        # Implement code to display seller information.
        print("Displaying seller information...")

    def display_product_list_and_prices(self):
        # Implement code to display product list and prices.
        print("Displaying product list and prices...")

    def view_members(self):
        # Implement code to view the list of members.
        print("Viewing members...")

    def remove_member(self, member_username):
        # Implement code to remove a member by username.
        print(f"Removing member {member_username}...")

    def remove_seller(self, seller_username):
        # Implement code to remove a seller by username.
        print(f"Removing seller {seller_username}...")

    def view_product_details(self, product_id):
        # Implement code to view product details by product ID.
        print(f"Viewing product details for product ID {product_id}...")

    def view_payment_details(self, user_id):
        # Implement code to view payment details for a user by user ID.
        print(f"Viewing payment details for user ID {user_id}...")

    def view_order_details(self, order_id):
        # Implement code to view order details by order ID.
        print(f"Viewing order details for order ID {order_id}...")

# Example usage:
if __name__ == "__main__":
    admin = Admin("admin", "1", "adminpassword")
    admin.register()

    # Perform admin actions
    admin.login("adminpassword")
    admin.display_seller_info()
    admin.display_product_list_and_prices()
    admin.view_members()
    admin.remove_member("user123")
    admin.remove_seller("seller456")
    admin.view_product_details("product789")
    admin.view_payment_details("user123")
    admin.view_order_details("order456")
    admin.logout()
