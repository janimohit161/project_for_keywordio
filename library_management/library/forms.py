from django import forms
from django.contrib.auth.models import User
from . import models

class AdminSigupForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        

class StudentUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']


class StudentExtraForm(forms.ModelForm):
    class Meta:
        model=models.StudentExtra
        fields=['enrollment','branch']
        
class BookForm(forms.ModelForm):
    class Meta:
        model=models.Book
        fields=['name','bookno','author','category']
class IssuedBookForm(forms.Form):
    
    bookno2=forms.ModelChoiceField(queryset=models.Book.objects.all(),empty_label="Name and bookno", to_field_name="bookno",label='Name and Bookno')
    enrollment2=forms.ModelChoiceField(queryset=models.StudentExtra.objects.all(),empty_label="Name and enrollment",to_field_name='enrollment',label='Name and enrollment')