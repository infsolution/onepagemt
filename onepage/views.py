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
	user = Perfil.objects.all().first()
	aboult = Aboult.objects.all().first()
	image_testimonial = ImageTestimonial.objects.all().first
	datas['aboult'] = aboult
	heros = Hero.objects.all()
	datas['heros'] = heros
	categorias = Categoria.objects.all()
	datas['categorias'] = categorias
	testimonials = Testimonial.objects.all()
	datas['testimonials'] = testimonials
	datas['image_testimonial'] = image_testimonial
	datas['detalhes'] = get_object(Detalhes)#get_detalhes()
	datas['galeria'] = get_object(Galeri)
	return render(request, 'onepage/index.html', {'datas':datas, 'user':user})
@login_required
def panel(request):
	#user = None
	#if request.user:
	#	user = User.objects.get(id=request.user.id)
	perfil = Perfil.objects.all().first()
	heros = Hero.objects.all()
	categorias = Categoria.objects.all()
	users = User.objects.all()#.exclude(id=request.user.id)
	testimonials = Testimonial.objects.all()
	form_aboult = AboultModelForm()
	form_hero = HeroModelForm()
	form_categoria = CategoriaModelForm()
	form_produto = ProdutoModelForm()
	form_perfil = PefilModelForm(instance=perfil)
	form_testimonial = TestimonialModelForm()
	detalhes = get_object(Detalhes)
	form_detalhes = DetalhesModelForm(instance=detalhes)
	galery = get_object(Galeri)
	form_fotos = FotoGaleriaModelFrom()
	form_galery = GaleriModelForm(instance=get_object(Galeri))

	return render(request, 'onepage/panel.html',{'form_aboult': form_aboult,
	'form_hero': form_hero, 'heros': heros, 'form_categoria':form_categoria, 
	'form_produto': form_produto, 'categorias':categorias, 'users':users,
	'form_perfil':form_perfil, 'perfil': perfil, 'form_testimonial':form_testimonial,
	'testimonials':testimonials, 'form_detalhes': form_detalhes, 'detalhes':detalhes,
	'form_fotos': form_fotos, 'form_galery':form_galery, 'galery':galery})


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

def get_object(object):
	obj = object.objects.all().first()
	if obj == None:
		obj = object()
		obj.save()
		return obj
	return obj

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
		return redirect('/panel')
	return redirect('/panel')


def message(request):
	if request.method == 'POST':
		user = User.objects.filter(telefone=request.POST['fone']).first()
		if user == None:
			new_user = User(Name=request.POST['name'], telefone=request.POST['fone'], email=request.POST['email'])
			new_user.save()
			message = Message(user=new_user, text=request.POST['message'])
			message.save()
			return HttpResponse("<p>Obrigado por sua mensagem "+new_user.Name+"! Em breve entraremos em contanto.</p>")
			
		else:
			message = Message(user=user, text=request.POST['message'])
			message.save()
			return HttpResponse("<p>Obrigado por sua mensagem "+user.Name+"! Em breve entraremos em contanto.</p>")
	else:
		return HttpResponse("<p>Methodo não permitido!</p>")
		
def perfil(request, perfil_id=0):
	if request.method == 'POST':
		try:
			if request.POST['action']:
				perfil = Perfil.objects.get(id=perfil_id)
				perfil.titulo = request.POST['titulo']
				perfil.descricao = request.POST['descricao']
				perfil.nome = request.POST['nome']
				perfil.cargo = request.POST['cargo']
				perfil.facebook = request.POST['facebook']
				perfil.twitter = request.POST['twitter']
				perfil.linkedin = request.POST['linkedin']
				perfil.instagran = request.POST['instagran']
				url = ''
				if request.FILES:
					url = save_image(request, 'foto')
					perfil.foto = url
				perfil.save()
				return redirect('/panel')
		except Exception as identifier:
			form = PefilModelForm(request.POST)
			if form.is_valid():
				model = form.save(commit=False)
				url = ''
				if request.FILES:
					url = save_image(request, 'foto')
				perfil = Perfil(titulo=model.titulo, descricao=model.descricao, nome=model.nome, cargo=model.cargo,
				facebook=model.facebook, twitter=model.twitter, linkedin=model.linkedin, instagran=model.instagran, foto=url)
				perfil.save()
				return redirect('/panel')

def testimonial(request, testimonial_id=0):
	if request.method == 'POST':
		try:
			if request.POST['action']:
				if request.POST['action'] == 'delete':
					testi = Testimonial.objects.get(id=testimonial_id)
					testi.delete()
					return redirect('/panel')
				if request.POST['action'] == 'edit':
					testi = Testimonial.objects.get(id=testimonial_id)
					testi.nome_cliente = request.POST['nome_cliente']
					testi.profissao = request.POST['profissao']
					testi.declaracao = request.POST['declaracao']
					url=''
					if request.FILES:
						url = save_image(request, 'foto')
					testi.foto = url
					testi.save()
					return redirect('/panel')


		except Exception as identifier:
			form = TestimonialModelForm(request.POST)
			if form.is_valid():
				model = form.save(commit=False)
				url = ''
				if request.FILES:
					url = save_image(request, 'foto')
				testimonial = Testimonial(nome_cliente=request.POST['nome_cliente'], profissao=request.POST['profissao'],
				declaracao=request.POST['declaracao'], foto=url)
				testimonial.save()
				return redirect('/panel')

def image(request):
	if request.FILES:
		image = ImageTestimonial(foto=save_image(request,'foto'))
		image.save()
		return redirect('/panel')
def image_calery(request):
	if request.FILES:
		galery = get_object(Galeri)
		image = FotoGaleria(galeria=galery, descricao_imagem=request.POST['descricao_imagem'], foto=save_image(request, 'foto'))
		image.save()
		return redirect('/panel')
def detail(request, detail_id):
	if request.method == 'POST':
		detail = Detalhes.objects.get(id=detail_id)
		detail.telefone = request.POST['telefone']
		detail.titulo_navbar = request.POST['titulo_navbar']
		detail.titulo_produtos = request.POST['titulo_produtos']
		detail.titulo_contatos = request.POST['titulo_contatos']
		detail.frase_contatos = request.POST['frase_contatos']
		detail.titulo_rodape = request.POST['titulo_rodape']
		detail.frase_rodape = request.POST['frase_rodape']
		detail.link_facebook = request.POST['link_facebook']
		detail.link_twitter = request.POST['link_twitter']
		detail.link_instagram = request.POST['link_instagram']
		detail.link_linkedin = request.POST['link_linkedin']
		url = ''
		if request.FILES:
			url = save_image(request, 'imagem_fundo_perfil')
		detail.imagem_fundo_perfil = url
		detail.save()
		return redirect('panel')
def edit_galery(request):
	if request.method == 'POST':
		galery = get_object(Galeri)
		galery.titulo = request.POST['titulo']
		galery.frase_galeria = request.POST['frase_galeria']
		galery.save()
		return redirect('/panel')
	else:
		return HttpResponse("<p>Method not allowed!</p>")
def del_image_galery(request, foto_id):
	if request.method == 'GET':
		foto = FotoGaleria.objects.get(id=foto_id)
		foto.delete()
		return redirect('/panel')

def delete_categoria(request, categoria_id):
	cat = Categoria.objects.get(id=categoria_id)
	cat.delete()
	return redirect('/panel')