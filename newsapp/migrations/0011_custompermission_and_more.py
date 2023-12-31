# Generated by Django 4.2.2 on 2023-06-25 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0010_remove_permissionrequest_permissions_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='permissionrequest',
            name='permissions',
        ),
        migrations.AddField(
            model_name='permissionrequest',
            name='permissions',
            field=models.ManyToManyField(to='newsapp.custompermission'),
        ),
    ]
