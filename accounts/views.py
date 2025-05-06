from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import Userform
from .models import User
from django.contrib import messages

# Create your views here.


def registerUser(request):
    if request.method == 'POST':
        # print(request.POST)
        form = Userform(request.POST)
        if form.is_valid():

            # craete the user using the form

            # password = form.cleaned_data['password']
            # user = form.save(commit=False)
            # user.set_password(password)
            # user.role = User.CUSTOMER
            # form.save()

            # create the user using create_user method

            first_name =  form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(first_name=first_name, last_name=last_name, username = username, email = email, password = password)
            user.role = User.CUSTOMER
            user.save()
            # print('user is created')
            
            messages.success(request, 'Your account is registered successfully!')
            return redirect('registerUser')
        else:
            print('invalid form')
            print(form.errors)
    else:
        form = Userform()
    context = {
        'form' : form
    }
    return render(request,'accounts/registerUser.html', context)

