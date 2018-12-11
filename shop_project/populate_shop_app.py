import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shop_project.settings')
import django
django.setup()

import random
from faker import Faker
from shop_app.models import Customer, Product

fakegen = Faker()
def generate_brand():
	brands["Nike","Dior","Gucci","Balanciage","NEw Balance","Adidas","GOldenGoose","Mcqueen","Prada","Louis Vuitton"]
	index=random.randint(0,9)
	return brands[index]

def generates_clients():
	for customer in range(1000):
		customer=Customer.objects.get_or_create(first_name=fakegen.first_name(), last_name=fakegen.last_name(),email=fakegen.email(),password=fakegen.password())
		customer[0].save()
def generates_products():
	for product in range (50): 
		random_price=random.randint(5,1000)
		product= Product.objects.get_or_create(name=generate_brand,description=fakegen.text(),price=random_price)
		product[0].save()

def populate():
  generates_clients()
  generates_products()

if __name__ == '__main__':
  print('starting populate...')
  populate()
  print('done populating')


