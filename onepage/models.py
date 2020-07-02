from django.db import models

# Create your models here.
class Aboult(models.Model):
	h3title = models.CharField(max_length=55, null=False)
	content = models.TextField()
	url_video = models.CharField(max_length=255)
	capa_video = models.ImageField(blank=True, null=True, upload_to='media/')

class Hero(models.Model):
	titulo = models.CharField(max_length=45, null=False)
	conteudo = models.TextField()
	imagem_de_fundo = models.ImageField(blank=True, null=True, upload_to='media/')


class Categoria(models.Model):
	nome = models.CharField(max_length=255, null=False)
	def __str__(self):
		return self.name

class Produto(models.Model):
	nome = models.CharField(max_length=255, null=False)
	descricao = models.CharField(max_length=255, null=False)
	preco = models.DecimalField(max_digits=5, decimal_places=2)
	categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='produtos')




	