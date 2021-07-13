from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.http import HttpResponseRedirect
from .forms import SignUpRegistration, EditUserProfileForm, EditAdminProfileForm

# Create your views here.
# Sign up form
def sign_up(request):
    if request.method == 'POST':
        fm = SignUpRegistration(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'Account created!')
            fm = SignUpRegistration()    
    fm = SignUpRegistration()
    return render(request, 'enroll/sign_up.html', { 'form': fm })

# login form
def user_login(request):
    if not request.user.is_authenticated:
     if request.method == 'POST':
      fm = AuthenticationForm(request=request, data=request.POST)
      if fm.is_valid():
         uname = fm.cleaned_data['username']
         upass = fm.cleaned_data['password']
         user = authenticate(username = uname, password = upass)
         if user is not None:
          login(request,user)
          messages.success(request, "You have successfully logged in!")
          return HttpResponseRedirect('/profile/')
     else:
      fm = AuthenticationForm()
     return render(request, 'enroll/user_login.html', { 'form': fm })
    else:
     return HttpResponseRedirect('/profile/')

# Profile page
def user_profile(request):
    if request.user.is_authenticated:
     if request.method == 'POST':
      if request.user.is_superuser == True:
        fm = EditAdminProfileForm(request.POST, instance = request.user)
      else:
        fm = EditUserProfileForm(request.POST, instance = request.user)
      if fm.is_valid():
       fm.save()
       messages.success(request, "Updated Successfully!")
     else:
      if request.user.is_superuser == True:
       fm = EditAdminProfileForm(instance = request.user)
      else:
       fm = EditUserProfileForm(instance = request.user) 
     return render(request, 'enroll/user_profile.html' , {'name': request.user , 'form':fm})
    else:
     return HttpResponseRedirect('/login/')

# Logout
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')

# Change Password with old password
def user_change(request):
   if request.user.is_authenticated:
    if request.method == 'POST':
      fm = PasswordChangeForm(user=request.user, data=request.POST)
      if fm.is_valid():
       fm.save()
       update_session_auth_hash(request, fm.user)
       messages.success(request, "Password Changed successfully!")
       return HttpResponseRedirect('/profile/')
    else:
       fm = PasswordChangeForm( user=request.user )
    return render(request, 'enroll/change_pass.html', {'form':fm})
   else:
       return HttpResponseRedirect('/login/')  

# Change password without old password
def user_change1(request):
   if request.user.is_authenticated:
    if request.method == 'POST':
      fm = SetPasswordForm(user=request.user, data=request.POST)
      if fm.is_valid():
       fm.save()
       update_session_auth_hash(request, fm.user)
       messages.success(request, "Password Changed successfully!")
       return HttpResponseRedirect('/profile/')
    else:
       fm = SetPasswordForm( user=request.user )
    return render(request, 'enroll/change_pass1.html', {'form':fm})
   else:
       return HttpResponseRedirect('/login/')  