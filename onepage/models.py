from django.db import models

# Create your models here.
class Aboult(models.Model):
	h3title = models.CharField(max_length=55, null=False)
	content = models.TextField()
	url_video = models.CharField(max_length=255)
	capa_video = models.ImageField(blank=True, null=True, upload_to='media/images/')