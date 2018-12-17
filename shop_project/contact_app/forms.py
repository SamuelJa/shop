from django import forms
from contact_app.models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['subject', 'email', 'text']
        widgets = {
        	'subject': forms.TextInput(attrs={
        	    'id':'comment-subject',
        	    'placeholder':'subject',
        	    'required': True
        	    }),
        	'email': forms.EmailInput(attrs={
        	    'id':'comment-email',
        	    'placeholder':'email',
        	    'required': True
        	    }),        
        	'text': forms.Textarea(attrs={
        	    'id':'comment-text',
        	    'placeholder':'text',
        	    'required': True
        	    })
        }