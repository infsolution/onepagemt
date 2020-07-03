# Generated by Django 3.0.7 on 2020-06-30 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aboult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('h3title', models.CharField(max_length=55)),
                ('content', models.TextField()),
                ('url_video', models.CharField(max_length=255)),
                ('capa_video', models.ImageField(blank=True, null=True, upload_to='media/images/')),
            ],
        ),
    ]