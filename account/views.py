from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views.generic import View,FormView,CreateView
from .forms import *
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages


# Create your views here.
# class homepage(View):
#     def get(self,request):
#         form=LoginForm
#         return render(request,"home.html",{"form":form})

class homepage(FormView):
    template_name="home.html"
    form_class=LoginForm

    def post(self,request,*args,**kwargs):
        form_data=LoginForm(data=request.POST)
        if form_data.is_valid():
            us=form_data.cleaned_data.get("username")
            pswd=form_data.cleaned_data.get("password")
            user=authenticate(request,username=us,password=pswd)
            if user:
                login(request,user)
                messages.success(request,"login successful")
                return redirect('custhome')
            else:
                messages.error(request,"Login failed !")
                return redirect('h')
        return render(request,"home.html",{"form":form_data})    
            
    
# class RegView(View):
#     def get(self,request):
#         form=Regform
#         return render(request,"regform.html",{"form":form})
#     def post(self,request):
#         form_data=Regform(data=request.POST)
#         if form_data.is_valid():
#            form_data.save()
#            return redirect("h")
#         return render (request,"regform.html",{"form":form_data})

class RegView(CreateView):
    template_name="regform.html"
    form_class=Regform
    model=User
    success_url=reverse_lazy("h")

    def form_valid(self,form):
        messages.success(self.request,"registration successful!!")
        return super().form_valid(form)
    

class LogoutView(View):
    def get(self,request):
        logout (request)
        return redirect ("h") 
        