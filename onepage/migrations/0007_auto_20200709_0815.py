# Generated by Django 3.0.7 on 2020-07-09 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onepage', '0006_auto_20200709_0802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='declaracao',
            field=models.TextField(),
        ),
    ]