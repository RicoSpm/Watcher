# Generated by Django 3.0.2 on 2020-03-16 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_leak', '0006_pastid'),
    ]

    operations = [
        migrations.AddField(
            model_name='alert',
            name='content',
            field=models.TextField(default=''),
        ),
    ]