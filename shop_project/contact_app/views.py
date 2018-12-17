from django.shortcuts import render , redirect
from contact_app.models import Contact
from contact_app.forms import ContactForm

# Create your views here.
def contact(request):
	if request.method=='POST':
		contact = Contact.objects.get_or_create(subject=request.POST.get('subject'),email = request.POST.get('email'),text = request.POST.get('text'))
		return redirect('contact_succes/')

	contact_form = ContactForm()
	return render(request,'contact.html', context={ 'contact_form':contact_form})
	
def contact_succes(request):
	return render(request,'contact_succes.html')