from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
import re
class SignupForm(forms.Form):
    email = forms.EmailField(max_length=50,required=True,label="Email")
    username = forms.CharField(max_length=15,required=True,label="Username")
    password = forms.CharField(widget=forms.PasswordInput,max_length=30,required=True,)
    confirm_password = forms.CharField(widget=forms.PasswordInput,max_length=30,required=True)

    label_suffix = ''

    def clean_email(self):

        email = self.cleaned_data['email']
        user_model = get_user_model()

        if user_model.objects.filter(email=email).exists():
            raise ValidationError("user with this email already exists")

        return email


    def clean_username(self):
        pattern = r"^[a-zA-Z0-9_]{3,20}$"
        username = self.cleaned_data['username']

        if re.match(pattern, username)==False:
            raise ValidationError("invalid username")


        user_model = get_user_model()
        if user_model.objects.filter(username=username).exists():
            raise ValidationError("user with this username already exists")
        return username
            
    def clean_confirm_password(self):

        password = self.cleaned_data['password']
        password_confirm = self.cleaned_data['confirm_password']

        if password != password_confirm:
            raise ValidationError("passwords didn't match")

        return password_confirm
        


class LoginForm(forms.Form):
    email = forms.EmailField(max_length=50,required=True)
    password = forms.CharField(widget=forms.PasswordInput,required=True)


        
    
