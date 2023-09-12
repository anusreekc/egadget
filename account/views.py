from django.shortcuts import render,redirect
from django.urls import reverse_lazy

from django.views.generic import View,FormView,CreateView
from .forms import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout




# Create your views here.
# class EHomeView(View):
#     def get(self,request):
#         form=LoginForm()
#         return render(request,"Ehome.html",{"form":form})

class EHomeView(FormView):
    template_name="Ehome.html"
    form_class=LoginForm


    def post(self,request,*args,**kwargs):
        form_data=LoginForm(data=request.POST)
        if form_data.is_valid():
            us=form_data.cleaned_data.get("username")
            pswd=form_data.cleaned_data.get("password")
            user=authenticate(request,username=us,password=pswd)
            if user:
                login(request,user)
                messages.success(request,'login successfull')
                return redirect('custhome')
            else:
                messages.error(request,"sign in failed!!!")
                return redirect('home')
        return render(request,"Ehome.html",{"form":form_data})    
    
# class RegView(View):
#     def get(self,request):
#         form=RegForm()
#         return render(request,"reg.html",{"form":form})
class RegView(CreateView):
    template_name="reg.html"
    form_class=RegForm
    model=User
    success_url=reverse_lazy('home')

    def form_valid(self,form):
        messages.success(self.request,"registration successfull!!")
        return super().form_valid(form)

    
    # def post(self,request):
    #     form_data=RegForm(data=request.POST)
    #     if form_data.is_valid():
    #         form_data.save()
    #         messages.success(request,"sign up completed!")
    #         return redirect('home')
        
    #     return render(request,"reg.html",{"form":form_data})
class LgOutView(View):
    def get(self,request):
        logout(request) 
        return redirect("home")   

