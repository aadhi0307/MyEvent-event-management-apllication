# Generated by Django 4.1.7 on 2023-08-10 17:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0019_alter_service_c_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='c_name',
            new_name='x_name',
        ),
    ]
