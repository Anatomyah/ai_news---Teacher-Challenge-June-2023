# Generated by Django 4.2.2 on 2023-06-30 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0017_alter_article_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='description',
            field=models.CharField(default=1, max_length=250),
        ),
    ]
