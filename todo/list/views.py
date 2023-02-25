
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterUserForm, MessageForm
from .models import message
from django.views.generic import DeleteView

def register_user(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            email = form.cleaned_data['email']
            user = authenticate(username=username, password=password, email=email)
            login(request,user)
            messages.success(request, ("Registration Successful!"))
            return redirect('/')
    else:
        form = RegisterUserForm()
        
    return render(request,'register.html',{'form':form})

def login_user(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('details')
		else:
			messages.success(request, ("There Was An Error Logging In, Try Again..."))	
			return redirect('login')	


	else:
		return render(request, 'login.html', {})


def about(request):
    form = MessageForm()
    if request.method == 'POST':
         form = MessageForm(request.POST)
         if form.is_valid():
            form.save()
            form = MessageForm()
            return redirect('details')
    return render(request,'about.html',{'form':form})
    
             
def details(request):
    obj = message.objects.all()
    context ={
        'obj': obj,
    }
    
    return render(request, 'details.html',context)



    
def logout_user(request):
    logout(request)
    return redirect('/')


def Update(request, id):
    obj = message.objects.get(id=id)
    form = MessageForm()
    if request.method =='POST':
        form = MessageForm(request.POST, instance = obj)
        if form.is_valid():
            form.save()
            form = MessageForm() 
            return redirect('details')

    return render(request,'update.html',{'form':form, 'obj':obj})

def Delete(request, id):
    obj = message.objects.get(id=id)
    obj.delete()
    return redirect('')