from django.shortcuts import render
from shop_app.models import Product, Customer , Maillot , Comment
from shop_app.forms import CommentForm
import datetime


def index(request):
  products = Product.objects.all()
  return render(request, 'index.html', context={ 'products': products })


def product(request, product_id):
  product = Product.objects.get(id=product_id)
  comments=Comment.objects.all()
  return render(request, 'product.html', context={ 'product': product,'comments':comments})


def customers(request):
  customers = Customer.objects.all()
  return render(request, 'customers.html', context={ 'customers': customers })


def customer(request, customer_id):
  customer = Customer.objects.get(id=customer_id)
  return render(request, 'customer.html', context={ 'customer': customer })

def maillots(request):
	maillots=Maillot.objects.all()
	return render(request,'maillots.html', context={'maillots':maillots })

def maillot(request , maillot_id):
	maillot=Maillot.objects.get(id=maillot_id)
	return render ( request, 'maillot.html', context={'maillot':maillot})

def comments(request):
	comments=Comment.objects.all()
	return render(request,'comments.html', context={'comments':comments})

def comment(request,comment_id):
	comment=Comment.objects.get(id=comment_id)
	return render (request,'comment.html', context={'comment':comment})

def comment_form(request,product_id):
	if request.method=='POST':
		print('#####')
		username = request.POST.get('username')
		text = request.POST.get('text')
		product = Product.objects.get(id=product_id)
		date = datetime.datetime.now()
		comment = Comment.objects.get_or_create(username=username,text=text,product=product,date=date)
		comment.save()

	comment_form=CommentForm()
	return render ( request , 'comment_form.html', context={'comment_form':comment_form})




















