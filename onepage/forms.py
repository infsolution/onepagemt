# -*- coding: utf-8 -*-
from django.forms import ModelForm, Textarea
from django import forms 
from django.contrib.auth.models import User
from onepage.models import *



class AboultModelForm(forms.ModelForm):
    class Meta:
        model = Aboult
        fields = ['h3title','content', 'url_video', 'capa_video']
        widgets = {
            'h3title': forms.TextInput(attrs={'class': 'form-control', 'maxlength':55}),
            'content':Textarea(attrs={'class':'form-control', 'maxlength':1250, 'rows':5, 'cols':40}),
            'url_video':forms.TextInput(attrs={'class':'form-control', 'maxlength':255}),
            'capa_video': forms.FileInput(attrs={'class':'form-control'})
        }

        error_messages={
            'h3title':{
                'required':'Campo obrigatório'
            },
            'content':{
                'required':'Campo obrigatório'
            },
        }

class HeroModelForm(forms.ModelForm):
    class Meta:
        model = Hero
        fields = ['titulo','conteudo','imagem_de_fundo']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'maxlength':55}),
            'conteudo': Textarea(attrs={'class':'form-control', 'maxlength':550, 'rows':5, 'cols':40}),
            'imagem_de_fundo': forms.FileInput(attrs={'class':'form-control'})
        }

class CategoriaModelForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome']
        widgets = {
            'nome': forms.TextInput(attrs={'class':'form-control', 'maxlength':255}),
        }


class ProdutoModelForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'descricao', 'preco', 'categoria']
        widgets = {
            'nome': forms.TextInput(attrs={'class':'form-control', 'maxlength':255}),
            'descricao': forms.TextInput(attrs={'class':'form-control', 'maxlength':255}),
            'preco': forms.NumberInput(attrs={'class':'form-control', 'maxlength':255}),
            'categoria':forms.Select(attrs={'class':'form-control'})
        }
class PefilModelForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['id','titulo', 'descricao', 'nome', 'cargo', 'facebook', 'twitter', 'linkedin', 'instagran', 'foto']
        widgets = {
            'titulo': forms.TextInput(attrs={'class':'form-control', 'maxlength':255}),
            'descricao': forms.TextInput(attrs={'class':'form-control', 'maxlength':255}),
            'nome': forms.TextInput(attrs={'class':'form-control', 'maxlength':255}),
            'cargo': forms.TextInput(attrs={'class':'form-control', 'maxlength':255}),
            'facebook': forms.TextInput(attrs={'class':'form-control', 'maxlength':255}),
            'twitter': forms.TextInput(attrs={'class':'form-control', 'maxlength':255}),
            'linkedin': forms.TextInput(attrs={'class':'form-control', 'maxlength':255}),
            'instagran': forms.TextInput(attrs={'class':'form-control', 'maxlength':255}),
            'foto': forms.FileInput(attrs={'class':'form-control'}),
        }