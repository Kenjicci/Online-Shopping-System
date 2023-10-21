class Admin():
  def __init__(self, username, password):
    self.username = username
    self.password = password

  def login(self):
    while self.password != self.password:
      print("Invalid Password")
      

