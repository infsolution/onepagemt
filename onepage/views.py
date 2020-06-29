from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.shortcuts import render
def index(request):
	return render(request, 'onepage/index.html')

@login_required
def update(request):
	if request.method == 'POST':
		pass
	return render(request, 'onepage/form.html')
