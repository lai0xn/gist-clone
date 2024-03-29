from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.decorators import method_decorator
from django.views import View
from .models import Gist
from . import forms


@login_required(login_url="/login")
def home_page(request):
    gists = Gist.objects.filter(user=request.user)
    context = {
        "gists":gists
    }
    return render(request,"index.html",context=context)



def gist_view(request,pk):
    gist = get_object_or_404(Gist,id=pk)
    file_content_bytes = gist.file.read()
    file_content = file_content_bytes.decode('utf-8')
    context = {
        "gist":gist,
        "content":file_content,
        
    }
    return render(request,"gist.html",context=context)
@method_decorator(login_required(login_url="/login"),name="dispatch")
class CreateGist(View):
    form_class = forms.GistForm
    def get(self,request,*args,**kwargs):
        form = self.form_class()
        context = {
            "form":form
        }
        return render(request,"create_gist.html",context)


    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST,request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            is_private = form.cleaned_data['is_private']
            file = form.cleaned_data['file']
            Gist.objects.create(user=request.user,
                                title=title,
                                description=description,
                                is_private=is_private,
                                file=file) 
            messages.info(request,"gist created successfully") 
            return redirect("home")
        return render(request,'create_gist.html',{"form":form})

