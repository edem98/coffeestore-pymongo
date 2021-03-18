

class Product:

    def __init__(self,name, price, country, id=None):
        self.name = name
        self.price = price
        self.country = country
        self.id = id


    def get_product(self):
        if self.id is None:
            return {
                "name": self.name,
                "price": self.price,
                "country": self.country
            }
        return {
            "name" : self.name,
            "price" : self.price,
            "country" : self.country,
            "id" : self.id,
        }


    def __str__(self):
        return self.name +" "+ str(self.price)+" "+str(self.id)