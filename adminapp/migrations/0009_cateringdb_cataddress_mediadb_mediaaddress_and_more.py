# Generated by Django 4.1.7 on 2023-08-09 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0008_alter_transportationdb_transdescription'),
    ]

    operations = [
        migrations.AddField(
            model_name='cateringdb',
            name='catAddress',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='mediadb',
            name='mediaAddress',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='transportationdb',
            name='transAddress',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
