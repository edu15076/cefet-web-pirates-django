# Generated by Django 4.1.7 on 2023-04-01 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pirates', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tesouro',
            name='img_tesouro',
            field=models.ImageField(upload_to='imgs', verbose_name='Imagem'),
        ),
    ]
