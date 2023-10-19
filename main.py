class Customer():
  def __init__(self, idnumber, username, password, email, address):
    #try to inherit the details from the parent class
    self.idnumber = idnumber
    self.username = username
    self.password = password
    self.email = email
    self.address = address
  
  def login(self):
    return("Successfully Log in!")
  #paste here the next process
  def buy(self):
    pass
  #try to paste the product list here
  def chat(self):
    pass 
  def add_to_cart(self):
    pass
  def checkout(self):
    pass
  def cancel_order(self):
    pass
  def logout(self):
    pass
