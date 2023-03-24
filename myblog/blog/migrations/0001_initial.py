# Generated by Django 4.1.7 on 2023-02-16 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('description', models.TextField(verbose_name='Text')),
                ('author', models.CharField(max_length=100, verbose_name='Name')),
                ('date', models.DateField(verbose_name='Date')),
            ],
        ),
    ]