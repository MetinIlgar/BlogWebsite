# Generated by Django 4.0.3 on 2022-03-06 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0008_blogpost_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='image',
            field=models.ImageField(blank=True, upload_to='media', verbose_name='Resim'),
        ),
    ]
