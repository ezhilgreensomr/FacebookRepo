from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=15)
    password = forms.CharField(max_length=10)
    confirm_password = forms.CharField(max_length=10)
    email = forms.EmailField()
    phoneNo = forms.IntegerField()
    address = forms.CharField(max_length=25)
    age = forms.IntegerField()



