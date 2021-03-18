

class CustomerModel:

    def __init__(self, connection):
        self.connection = connection


    def insertCustomer(self,customer):
        try:
            customers = self.connection.customers
            customer_id = customers.insert_one(customer.get_customer()).inserted_id
            customer.id = customer_id
            return customer
        except Exception as e:
            print(e)

    def getCustomers(self):
        try:
            customers = self.connection.customers
            return customers.find()
        except Exception as e:
            print(e)
