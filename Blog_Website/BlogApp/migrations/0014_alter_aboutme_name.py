# Generated by Django 4.0.3 on 2022-03-06 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0013_alter_aboutme_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutme',
            name='name',
            field=models.CharField(max_length=30, verbose_name='İsim'),
        ),
    ]
