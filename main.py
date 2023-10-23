class User:
    user_database = {}

    def __init__(self, user_id, username, password):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.logged_in = False
        User.user_database[user_id] = {
            'username': username,
            'password': password
        }

    def register(self):
        User.user_database[self.user_id] = {
            'username': self.username,
            'password': self.password
        }
        print(f"User {self.username} registered successfully.")

    def login(self, entered_password):
        if self.password == entered_password:
            self.logged_in = True
            print(f"User {self.username} logged in.")
        else:
            print("Login failed. Incorrect password.")

    def logout(self):
        self.logged_in = False
        print(f"User {self.username} logged out.")

    @classmethod
    def get_user_by_id(cls, user_id):
        return cls.user_database.get(user_id)


class Customer(User):
    def __init__(self, idnumber, username, password, email, address):
        super().__init__(idnumber, username, password)
        self.email = email
        self.address = address

    def buy(self):
        print("Customer is buying.")

    def chat(self):
        print("Customer is chatting.")

    def add_to_cart(self):
        print("Customer is adding items to the cart.")

    def checkout(self):
        print("Customer is checking out.")

    def cancel_order(self):
        print("Customer is canceling an order.")

# Example usage:
if __name__ == "__main__":
    # Create a customer
    customer1 = Customer("1", "customer123", "customerpassword", "customer@example.com", "123 Main St")

    # Register the customer
    customer1.register()

    # Attempt to login
    customer1.login("incorrect_password")  # Incorrect password

    # Correct login
    customer1.login("customerpassword")

    # Perform customer actions
    customer1.buy()
    customer1.chat()
    customer1.add_to_cart()
    customer1.checkout()
    customer1.cancel_order()

    # Logout
    customer1.logout()
