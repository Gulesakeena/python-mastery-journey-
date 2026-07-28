class Customer:
    def __init__(self,name,gender,address):
        self.name = name
        self.gender = gender 
        self.address = address
    def update_profle(self,updatd_name,new_city,new_pincode,new_state):
        self.name = updatd_name
        self.address.change_address(new_city,new_pincode,new_state)

class Address:
    def __init__(self,city,pincode,state):
        self.city = city
        self.pincode = pincode
        self.state = state

    def change_address(self,new_city,new_pincode,new_state):
        self.city = new_city
        self.state = new_state
        self.pincode = new_pincode

address = Address("wazirabad",52000,"gujrawala")
customer = Customer("ali","female",address)
customer.update_profle("ali","lahore",52000,'islamabad')
