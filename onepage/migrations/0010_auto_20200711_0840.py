# Generated by Django 3.0.7 on 2020-07-11 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onepage', '0009_auto_20200711_0828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detalhes',
            name='frase_rodape',
            field=models.CharField(default='Frase do rodapé', max_length=155),
        ),
        migrations.AlterField(
            model_name='detalhes',
            name='link_facebook',
            field=models.CharField(default='https://facebook.com/seuusuario/', max_length=155),
        ),
        migrations.AlterField(
            model_name='detalhes',
            name='link_instagram',
            field=models.CharField(default='https://instagram.com/seuusuario/', max_length=155),
        ),
        migrations.AlterField(
            model_name='detalhes',
            name='link_linkedin',
            field=models.CharField(default='https://linkedin.com/seuusuario/', max_length=155),
        ),
        migrations.AlterField(
            model_name='detalhes',
            name='link_twitter',
            field=models.CharField(default='https://twitter.com/seuusuario/', max_length=155),
        ),
        migrations.AlterField(
            model_name='detalhes',
            name='telefone',
            field=models.CharField(default='(88)888888888', max_length=20),
        ),
        migrations.AlterField(
            model_name='detalhes',
            name='titulo_contatos',
            field=models.CharField(default='Titulo da sessão contatos', max_length=155),
        ),
        migrations.AlterField(
            model_name='detalhes',
            name='titulo_navbar',
            field=models.CharField(default='Titulo da sua home', max_length=55),
        ),
        migrations.AlterField(
            model_name='detalhes',
            name='titulo_perfil',
            field=models.CharField(default='Titulo da sessão perfil', max_length=155),
        ),
        migrations.AlterField(
            model_name='detalhes',
            name='titulo_produtos',
            field=models.CharField(default='Titulo da sessão produtos', max_length=155),
        ),
        migrations.AlterField(
            model_name='detalhes',
            name='titulo_rodape',
            field=models.CharField(default='Titulo do redapé', max_length=155),
        ),
    ]
