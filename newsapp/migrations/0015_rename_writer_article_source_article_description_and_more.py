# Generated by Django 4.2.2 on 2023-06-30 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0014_article_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='writer',
            new_name='source',
        ),
        migrations.AddField(
            model_name='article',
            name='description',
            field=models.CharField(default='Test', max_length=250),
        ),
        migrations.AlterField(
            model_name='article',
            name='body',
            field=models.CharField(max_length=5000),
        ),
    ]
