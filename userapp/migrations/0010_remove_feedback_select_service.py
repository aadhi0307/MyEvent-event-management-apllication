# Generated by Django 4.1.7 on 2023-08-17 12:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0009_rename_service_feedback_select_service'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='select_service',
        ),
    ]