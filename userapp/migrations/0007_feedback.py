# Generated by Django 4.1.7 on 2023-08-15 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0006_rename_contactdb_contactdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=50, null=True)),
                ('feedbacks', models.TextField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
