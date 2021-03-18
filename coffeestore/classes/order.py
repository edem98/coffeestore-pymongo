import datetime

class Order:

    def __init__(self, customer, id=None):
        self.products = []
        self.customer = customer
        self.order_date = datetime.datetime.now()
        self.id = id


    def add_product(self,product):
        self.products.append(product)


    def get_order(self):

        # products = []
        #
        # for p in self.products:
        #     products.append(p.get_product())
        #
        # return {
        #     'customer': self.customer.get_customer(),
        #     'order_date': self.order_date,
        #     'products': products
        # }

        if self.id is None:
            return {
                'customer' : self.customer.get_customer(),
                'order_date' : self.order_date,
                'products' : [product.get_product() for product in self.products]
            }
        return {
            'customer' : self.customer.get_customer(),
            'order_date' : self.order_date,
            'id' : self.id,
            'products' : [product.get_product() for product in self.products]
        }


    def __str__(self):
        return str(self.customer) +" "+ str(self.id)