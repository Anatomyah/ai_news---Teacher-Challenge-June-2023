# Generated by Django 4.2.2 on 2023-06-30 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0015_rename_writer_article_source_article_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.CharField(choices=[('gen', 'General'), ('wor', 'World'), ('nat', 'Nation'), ('bus', 'Business'), ('tech', 'Technology'), ('ent', 'Entertainment'), ('spr', 'Sports'), ('sci', 'Science'), ('hel', 'Health')], default='gen', max_length=20),
        ),
    ]
