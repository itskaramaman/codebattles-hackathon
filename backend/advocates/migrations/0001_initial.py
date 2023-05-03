# Generated by Django 4.2.1 on 2023-05-03 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advocate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(upload_to='')),
                ('username', models.CharField(max_length=200, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('bio', models.TextField()),
                ('twitter', models.TextField()),
            ],
        ),
    ]