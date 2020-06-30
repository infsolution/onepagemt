from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
def index(request):
	return render(request, 'onepage/index.html')

def panel(request):
	user = User.objects.get(id=request.user.id)
	return render(request, 'onepage/panel.html',{'user':user})

@login_required
def update(request):
	if request.method == 'POST':
		pass
	return render(request, 'onepage/form.html')


def do_login(request):
	if request.method == 'POST':
		user = authenticate(username = request.POST['username'], password =  request.POST['password'])
		print(user)
		if user is not None:
			login(request,user)
			return redirect('/panel',user)
		else:
			return render(request, 'onepage/login.html', {'error':'Usuario ou senha inválidos'})
	return render(request, 'onepage/login.html')

def do_logout(request):
	logout(request)
	return redirect('/login')