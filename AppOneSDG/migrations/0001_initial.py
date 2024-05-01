# Generated by Django 4.2.3 on 2024-04-23 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('userId', models.AutoField(primary_key=True, serialize=False, verbose_name='User ID')),
                ('firstName', models.CharField(max_length=100, verbose_name='First name')),
                ('lastName', models.CharField(max_length=100, verbose_name='Last name')),
                ('username', models.CharField(max_length=100, unique=True, verbose_name='Username')),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='Email address')),
                ('contactNumber', models.CharField(max_length=100, verbose_name='Contact number')),
                ('emergencyContact', models.CharField(max_length=100, verbose_name='Emergency contact')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='Date joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='Last login')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
