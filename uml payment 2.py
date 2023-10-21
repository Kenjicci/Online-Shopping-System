class PaymentSystem:
    def __init__(self, order_number, amount, total_amount):
        self.order_number = order_number
        self.amount = amount
        self.total_amount = total_amount
        self.payments = []  # List to store payment details

    def make_payment(self, payment_amount):
        if payment_amount <= 0:
            return "Payment amount must be greater than 0."
        if self.amount >= payment_amount:
            self.amount -= payment_amount
            self.payments.append(payment_amount)
            return f"Payment of ${payment_amount} made successfully."
        else:
            return "Insufficient funds for the payment."

    def refund(self, refund_amount):
        if refund_amount <= 0:
            return "Refund amount must be greater than 0."
        if refund_amount <= sum(self.payments):
            self.amount += refund_amount
            self.payments.remove(refund_amount)
            return f"Refund of ${refund_amount} processed successfully."
        else:
            return "Cannot refund more than the total payment amount."

    def view_payment(self):
        return f"Remaining amount: ${self.amount}"

    def view_details(self):
        return f"Order Number: {self.order_number}\nTotal Amount: ${self.total_amount}\nRemaining Amount: ${self.amount}\nPayments Made: ${', '.join(map(str, self.payments))}"
