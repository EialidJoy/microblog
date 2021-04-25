from django.shortcuts import render,redirect
from django.http import HttpResponse
# from microblog import socialsite
# Create your views here.
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User,auth
from django.contrib.auth import logout
# from django.contrib.auth.decorators import login_required

# def login(request):
# 	if request.method=='POST':
# 		username = request.POST['username']
# 	    password = request.POST['password']
# 	    user = authenticate(request, username=username, password=password)
# 	    if user is not None:
# 	        login(request, user)
# 	        # Redirect to a success page.
# 	        return redirect('home')
# 	        ...
# 	    else:
# 	        # Return an 'invalid login' error message.
# 	        return HttpResponse("Here's the text of the Web page.")

# 	else:
# 		return render(request,'accounts/login.html')

# @login_required(login_url='/accounts/login/')
def login(request):
	if request.method == 'POST':
		username=request.POST['username']
		password=request.POST['password']

		user=auth.authenticate(username=username,password=password)

		if user is not None:
			auth.login(request, user)
			return redirect("../../home")

		else:
			messages.info(request,'wrong email/password')
			return redirect('/accounts/login')

	else: 
		return render(request,'accounts/login.html')


def register(request):
    if request.method=='POST':              #if the request is post
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username taken')

            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email taken')
            else:
                user=User.objects.create_user(username=username,password=password1, email=email, first_name=first_name,last_name=last_name)
                user.save()
                messages.info(request, 'user created successfully')
                return redirect('../accounts/login')
                
        else:
            messages.info(request, 'password is not matching')
        return redirect('/accounts/register')
    else:
        return render(request,'accounts/register.html')  #if the request is GET 



def logout(request):
    if request.method=='POST':
        auth.logout(request)
        return redirect('../../home')

