# Generated by Django 4.2.1 on 2023-05-04 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advocates', '0003_alter_advocate_profile_pic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('bio', models.TimeField(blank=True, null=True)),
            ],
        ),
    ]