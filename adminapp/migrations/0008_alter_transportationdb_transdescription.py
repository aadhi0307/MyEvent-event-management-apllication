# Generated by Django 4.1.7 on 2023-08-08 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0007_alter_cateringdb_catrent_alter_mediadb_mediarent_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transportationdb',
            name='transDescription',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
