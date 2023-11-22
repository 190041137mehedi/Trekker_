# Generated by Django 3.2 on 2022-11-06 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AuthenApp', '0002_registertable'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadProfileFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserName', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('birthday', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('registrationDate', models.CharField(max_length=50)),
                ('cover', models.FileField(upload_to='')),
            ],
        ),
    ]
