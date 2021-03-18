

class OrderModel:

    def __init__(self, connection):
        self.connection = connection


    def insertOrder(self,order):
        try:
            orders = self.connection.orders
            order_id = orders.insert_one(order.get_order()).inserted_id
            order.id = order_id
            return order
        except Exception as e:
            print(e.message)

    def getOrders(self):
        try:
            orders = self.connection.orders
            return orders.find()
        except Exception as e:
            print(e.message)
