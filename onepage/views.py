from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from .forms import *
from .models import *
def index(request):
	datas = {}
	aboult = Aboult.objects.get(id=1)
	datas['aboult'] = aboult
	heros = Hero.objects.all()
	datas['heros'] = heros
	categorias = Categoria.objects.all()
	datas['categorias'] = categorias
	return render(request, 'onepage/index.html', {'datas':datas})
@login_required
def panel(request):
	user = User.objects.get(id=request.user.id)
	heros = Hero.objects.all()
	categorias = Categoria.objects.all()
	form_aboult = AboultModelForm()
	form_hero = HeroModelForm()
	form_categoria = CategoriaModelForm()
	form_produto = ProdutoModelForm()
	return render(request, 'onepage/panel.html',{'user':user, 'form_aboult': form_aboult,
	'form_hero': form_hero, 'heros': heros, 'form_categoria':form_categoria, 
	'form_produto': form_produto, 'categorias':categorias})


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
			aboult = Aboult(h3title=model.h3title, content=model.content, url_video=model.url_video, capa_video=url)
			aboult.save()
			return redirect('panel')
		error = 'Formulário invalido'
		return redirect('panel', error)

def add_hero(request, hero_id=0):
	if request.method == 'POST':
		try:
			if request.POST['action']:
				hero = Hero.objects.get(id=hero_id)
				hero.titulo = request.POST['titulo']
				hero.conteudo = request.POST['conteudo']
				print(request.FILES)
				if request.FILES:
					url = save_image(request, 'imagem_de_fundo')
					hero.imagem_de_fundo = url
				hero.save()
				return redirect('/panel')
		except Exception as identifier:
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

def add_produto(request, produto_id=0):
	if request.method == 'POST':
		form = ProdutoModelForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('/panel')
	else:
		if request.GET['action'] == 'delete':
			produto = Produto.objects.get(id=produto_id)
			produto.delete()
			return redirect('/panel')
		if request.GET['action'] == 'edit':
			produto = Produto.objects.get(id=produto_id)
			produto.nome = request.GET['nome']
			produto.descricao = request.GET['descricao']
			produto.preco = request.GET['preco']
			produto.save()
			return redirect('/panel')	
		return redirect('/panel')



def categoria(request):
	if request.method == 'POST':
		form = CategoriaModelForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('panel')
	return redirect('panel')


def message(request):
	if request.method == 'POST':
		user = User.objects.filter(telefone=request.POST['fone']).first()
		if user == None:
			new_user = User(Name=request.POST['name'], telefone=request.POST['fone'], email=request.POST['email'])
			new_user.save()
			message = Message(user=new_user, text=request.POST['message'])
			message.save()
			
		else:
			message = Message(user=user, text=request.POST['message'])
			message.save()
		return HttpResponse("<p>Obrigado por sua mensagem "+user.Name+"! Em breve entraremos em contanto.</p>")
	else:
		return HttpResponse("<p>Methodo não permitido!</p>")
		