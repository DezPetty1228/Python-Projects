# Generated by Django 4.1.7 on 2023-03-03 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campusApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='universitycampus',
            name='campus_ID',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
