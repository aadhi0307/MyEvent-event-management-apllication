# Generated by Django 4.1.7 on 2023-07-16 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='categorydata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(blank=True, max_length=50, null=True)),
                ('cimage', models.ImageField(blank=True, null=True, upload_to='category')),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
