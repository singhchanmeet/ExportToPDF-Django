# Generated by Django 4.1.4 on 2023-06-04 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('phone_number', models.CharField(max_length=10)),
                ('photograph', models.ImageField(upload_to='photographs')),
            ],
        ),
    ]
