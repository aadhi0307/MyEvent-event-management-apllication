# Generated by Django 4.1.7 on 2023-08-04 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='admindb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('mobile', models.IntegerField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='adminprofile')),
                ('pwd', models.CharField(blank=True, max_length=50, null=True)),
                ('cpwd', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]