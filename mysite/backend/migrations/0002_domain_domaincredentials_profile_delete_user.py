# Generated by Django 4.0.4 on 2022-06-13 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_contract', models.PositiveIntegerField()),
                ('profile', models.CharField(max_length=255)),
                ('domain', models.CharField(max_length=255, unique=True)),
                ('price', models.PositiveIntegerField()),
                ('active', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='DomainCredentials',
            fields=[
                ('id_contract', models.PositiveIntegerField()),
                ('domain', models.CharField(max_length=255, primary_key=True, serialize=False, unique=True)),
                ('seedPhrase', models.CharField(max_length=255)),
                ('secretKey', models.CharField(max_length=255)),
                ('publicKey', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wallet', models.CharField(max_length=255, unique=True)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('avatar', models.ImageField(null=True, upload_to='avatars')),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
