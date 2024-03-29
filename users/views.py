from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views import View
from users.models import User
from . import forms
# Create your views here.

class SignupView(View):
    form_class = forms.SignupForm

    def get(self,request,*args,**kwargs):
        form = self.form_class()
        context = {
            "form":form        }
        return render(request,"signup.html",context=context)

    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST)
        context = {
            'form':form
        }
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            User.objects.create_user(username=username,email=email,password=password) 
            return redirect('/')
        return render(request,'signup.html',context)

  

class LoginView(View):
    form_class = forms.LoginForm

    def get(self,request,*args,**kwargs):
        form = self.form_class()
        context = {
            "form":form        }
        return render(request,"login.html",context=context)

    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST)
        context = {
            'form':form
        }
        if form.is_valid():
            print(form.cleaned_data)
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(username=email,password=password)
            if user is not None:
                login(request,user)
                messages.success(request,"Login Successful")
                return redirect('/')

            else:
                messages.error(request,"Invalid Login")
                return redirect('login')
 

        return render(request,'login.html',context)
       

@login_required(login_url="/login")
def logout_view(request):
    logout(request)
    return redirect('/')
