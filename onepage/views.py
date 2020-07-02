from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import *
from .models import *
def index(request):
	datas = {}
	aboult = Aboult.objects.get(id=1)
	datas['aboult'] = aboult
	heros = Hero.objects.all()
	datas['heros'] = heros
	return render(request, 'onepage/index.html', {'datas':datas})

def panel(request):
	user = User.objects.get(id=request.user.id)
	heros = Hero.objects.all()
	form_aboult = AboultModelForm()
	form_hero = HeroModelForm()
	form_categoria = CategoriaModelForm()
	form_produto = ProdutoModelForm()
	return render(request, 'onepage/panel.html',{'user':user, 'form_aboult': form_aboult,
	'form_hero': form_hero, 'heros': heros, 'form_categoria':form_categoria, 'form_produto': form_produto})

@login_required
def update(request):
	if request.method == 'POST':
		pass
	return render(request, 'onepage/form.html')


def do_login(request):
	if request.method == 'POST':
		user = authenticate(username = request.POST['username'], password =  request.POST['password'])
		if user is not None:
			login(request,user)
			return redirect('/panel',user)
		else:
			return render(request, 'onepage/login.html', {'error':'Usuario ou senha inválidos'})
	return render(request, 'onepage/login.html')

def do_logout(request):
	logout(request)
	return redirect('/login')

def save_image(request, image_file):
	for image in request.FILES.getlist(image_file):
		up_image = image
		fs = FileSystemStorage()
		name = fs.save(up_image.name, up_image)
		return fs.url(name)

def add_aboult(request):
	if request.method == 'POST':
		form = AboultModelForm(request.POST)
		if form.is_valid():
			model = form.save(commit=False)
			url = ''
			if request.FILES:
				url = save_image(request, 'capa_video')
				'''for image in request.FILES.getlist('capa_video'):
					up_image = image
					fs = FileSystemStorage()
					name = fs.save(up_image.name, up_image)
					url = fs.url(name)'''
			aboult = Aboult(h3title=model.h3title, content=model.content, url_video=model.url_video, capa_video=url)
			aboult.save()
			return redirect('panel')
		error = 'Formulário invalido'
		return redirect('panel', error)

def add_hero(request, hero_id=0):
	if request.method == 'POST':
		form = HeroModelForm(request.POST)
		if form.is_valid():
			model = form.save(commit=False)
			url = ''
			if request.FILES:
				url = save_image(request, 'imagem_de_fundo')
			hero = Hero(titulo=model.titulo, conteudo=model.conteudo, imagem_de_fundo=url)
			hero.save()
			return redirect('panel')
		error = 'Formulário invalido'
		return redirect('panel', error)
	else:
		if request.GET['action'] == 'delete':
			hero = Hero.objects.get(id=hero_id)
			hero.delete()
			return redirect('/panel')
		if request.GET['action'] == 'edit': 
			hero = Hero.objects.get(id=hero_id)
			hero.title = request.GET['titulo']
			hero.conteudo = request.GET['conteudo']
			if request.FILES:
				url = save_image(request, 'imagem_de_fundo')
			hero.save()
			return redirect('/panel')


def add_produto(request):
	pass



def categoria(request):
	if request.method == 'POST':
		form = CategoriaModelForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('panel')
	return redirect('panel')