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