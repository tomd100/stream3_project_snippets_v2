from django.shortcuts import render, redirect, reverse, HttpResponseRedirect, get_object_or_404
from django.contrib import auth, messages
from .forms import UserLoginForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required

from .models import UserProfile

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

#-------------------------------------------------------------------------------

def home_page(request):
    return render(request, 'index.html')
    
#-------------------------------------------------------------------------------

def logout(request):
    auth.logout(request);                                                      
    messages.success(request, "You have successfully logged out")
    return redirect(home_page);
    
#-------------------------------------------------------------------------------

def login(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password'])
            if user is not None:
                auth.login(request, user);
                return redirect(home)
            else:
                messages.success(request, "Your user name or password was not recognised ", extra_tags='danger') 
    else:
        form = UserLoginForm();
    return render(request, "login.html", {'form': form})    
   
#-------------------------------------------------------------------------------    

def register(request):
    if request.method=="POST":
        form = UserRegistrationForm(request.POST);
        if form.is_valid():
            user = form.save();
            user = auth.authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'])
            if user is not None:
                return redirect(login)
                messages.success(request, "You have successfully registered")   
                
                # auth.login(request, user);
                
                # if request.GET and request.GET['next'] != "":
                #     next = request.GET["next"];
                #     return HttpResponseRedirect(next);
                # else:
                #     return redirect(login);
                
            # return redirect(login)      
    else:
        form = UserRegistrationForm();

    return render(request, "register.html", {'form': form})
    
#-------------------------------------------------------------------------------

@login_required(login_url="/accounts/login")
def home(request):
    return render(request, "home.html");

#-------------------------------------------------------------------------------

@login_required(login_url="/accounts/login")
def profile(request):
    return render(request, "profile.html");

#------------------------------------------------------------------------------- 

class SubscribeListView(LoginRequiredMixin, ListView):
    # form_class = 'SubscribeForm'
    model = UserProfile
    Fields=['sub_type']
    
#------------------------------------------------------------------------------- 