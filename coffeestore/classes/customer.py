

class Customer:

    def __init__(self,first_name, last_name,gender, phone_number=None, id=None):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.id = id
        self.phone_number = phone_number

    def get_customer(self):
        if self.id is None:
            return {
                "first_name": self.first_name,
                "last_name": self.last_name,
                "gender": self.gender,
                "phone_number": self.phone_number,
            }
        return {
            "first_name" : self.first_name,
            "last_name" : self.last_name,
            "gender" : self.gender,
            "phone_number" : self.phone_number,
            "id" : self.id,
        }

    def __str__(self):
        return self.first_name +" "+ self.last_name