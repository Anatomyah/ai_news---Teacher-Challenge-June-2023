# Generated by Django 4.2.2 on 2023-06-23 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='body',
            field=models.CharField(max_length=500),
        ),
    ]