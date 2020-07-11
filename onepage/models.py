from django.db import models

# Create your models here.
class Aboult(models.Model):
	h3title = models.CharField(max_length=55, null=False)
	content = models.TextField()
	url_video = models.CharField(max_length=255)
	capa_video = models.ImageField(blank=True, null=True, upload_to='media/')
	class Meta:
		ordering = ('-id',)

class Hero(models.Model):
	titulo = models.CharField(max_length=45, null=False)
	conteudo = models.TextField()
	imagem_de_fundo = models.ImageField(blank=True, null=True, upload_to='media/')


class Categoria(models.Model):
	nome = models.CharField(max_length=255, null=False)
	def __str__(self):
		return self.nome

class Produto(models.Model):
	nome = models.CharField(max_length=255, null=False)
	descricao = models.CharField(max_length=255, null=False)
	preco = models.DecimalField(max_digits=5, decimal_places=2)
	categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='produtos')
	def __str__(self):
		return self.nome

class User(models.Model):
	Name = models.CharField(max_length=255, null=False)
	telefone = models.CharField(max_length=255, null=False, unique=True)
	email = models.CharField(max_length=255, null=False, unique=True)
	created_at = models.DateField(auto_now_add=True)
	def __str__(self):
		return self.Name

class Message(models.Model):
	user = models.ForeignKey(User, on_delete= models.CASCADE, related_name='messages')
	text = models.TextField()
	created_at = models.DateField(auto_now_add=True)
	def __str__(self):
		return self.text
class Perfil(models.Model):
	titulo = models.CharField(max_length=155, null=False)
	descricao = models.CharField(max_length=255, null=False)
	nome = models.CharField(max_length=255, null=False)
	cargo = models.CharField(max_length=55, null=False)
	facebook = models.CharField(max_length=255, null=False)
	twitter = models.CharField(max_length=255, null=False)
	linkedin = models.CharField(max_length=255, null=False)
	instagran = models.CharField(max_length=255, null=False)
	foto = models.ImageField(blank=True, null=True, upload_to='media/')
	def __str__(self):
		return self.nome

class Testimonial(models.Model):
	nome_cliente = models.CharField(max_length=155, null=False)
	profissao = models.CharField(max_length=155, null=False)
	declaracao = models.TextField(null=False)
	foto = models.ImageField(blank=True, null=True, upload_to='media/')
	def __str__(self):
		return self.nome_cliente
	class Meta:
		ordering = ('-id',)

class ImageTestimonial(models.Model):
	foto = models.ImageField(blank=True, null=True, upload_to='media/')
	class Meta:
		ordering = ('-id',)

class Detalhes(models.Model):
	telefone = models.CharField(max_length=20, null=False, default="(88)888888888")
	titulo_navbar = models.CharField(max_length=55, null=False, default="Titulo da sua home")
	titulo_produtos = models.CharField(max_length=155, null=False, default="Titulo da sessão produtos")
	titulo_contatos = models.CharField(max_length=155, null=False, default="Titulo da sessão contatos")
	frase_contatos = models.CharField(max_length=255, null=False, default="Frase da sessão contatos")
	titulo_rodape = models.CharField(max_length=155, null=False, default="Titulo do redapé")
	frase_rodape = models.CharField(max_length=155, null=False, default="Frase do rodapé")
	link_facebook = models.CharField(max_length=155, null=False, default="https://facebook.com/seuusuario/")
	link_twitter = models.CharField(max_length=155, null=False, default="https://twitter.com/seuusuario/")
	link_instagram = models.CharField(max_length=155, null=False, default="https://instagram.com/seuusuario/")
	link_linkedin = models.CharField(max_length=155, null=False, default="https://linkedin.com/seuusuario/")
	imagem_fundo_perfil = models.ImageField(blank=True, null=True, upload_to='media/')
	class Meta:
		ordering = ('-id',)
class Galeri(models.Model):
	titulo =  models.CharField(max_length=155, null=False, default="Titulo da sua Galeria")
	frase_galeria =  models.CharField(max_length=255, null=False, default="Frase da sua Galeria")
	def __str__(self):
		return self.titulo
	class Meta:
		ordering = ('-id',)
	
class FotoGaleria(models.Model):
	galeria = models.ForeignKey(Galeri, on_delete= models.CASCADE, related_name='fotos')
	descricao_imagem = models.CharField(max_length=99, null=True, default="descrição da imagem")
	foto = models.ImageField(blank=True, null=True, upload_to='media/') 
	def __str__(self):
		return self.descricao_imagem