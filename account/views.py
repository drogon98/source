from django.shortcuts import render,reverse
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth import login,authenticate
from .forms import ChangeProfileForm

def home(request):
    return render(request,"account/home.html",{})

def register(request):
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            #username=form.cleaned_data.get("username")
            #raw_password=form.cleaned_data.get("password")
            #user=authenticate(username=username,password=raw_password)
            #login(request,user)
            return HttpResponseRedirect(reverse("login"))
    else:
        form=UserCreationForm()
    return render(request,"account/signup.html",{'form':form})


def change_profile(request):
    if request.method=="POST":
        form=ChangeProfileForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("home"))
    else:
        form=ChangeProfileForm(instance=request.user)
    return render(request,"account/change_prof.html",{'form':form})
