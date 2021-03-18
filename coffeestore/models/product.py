

class ProductModel:

    def __init__(self, connection):
        self.connection = connection


    def insertProduct(self,product):
        try:
            products = self.connection.products
            product_id = products.insert_one(product.get_product()).inserted_id
            product.id = product_id
            return product
        except Exception as e:
            print(e.message)

    def getProducts(self):
        try:
            products = self.connection.products
            return products.find()
        except Exception as e:
            print(e.message)
