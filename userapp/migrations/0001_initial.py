# Generated by Django 4.1.7 on 2023-08-13 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Userdata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('pwd', models.CharField(blank=True, max_length=50, null=True)),
                ('cpwd', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
