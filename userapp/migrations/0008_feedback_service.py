# Generated by Django 4.1.7 on 2023-08-15 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0007_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='service',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
