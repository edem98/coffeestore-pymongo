from connect import db
from models.product import ProductModel
from models.customer import CustomerModel
from models.order import OrderModel
from classes.product import Product
from classes.customer import Customer
from classes.order import Order

# create prodcut model
pm = ProductModel(db)
# create a product
# product = Product("Pinon",5000,"Togo")
# insert the product
# product = pm.insertProduct(product)

products = pm.getProducts()
product_list = []

for product in products:
    product_list.append(Product(product['name'],product['price'],product['country'],product['_id']))

cm = CustomerModel(db)
customer = Customer("Serge","Kossi","M","92639417")
customer = cm.insertCustomer(customer)

om = OrderModel(db)
order = Order(customer)

for product in product_list:
    order.add_product(product)

order = om.insertOrder(order)

print(order)




