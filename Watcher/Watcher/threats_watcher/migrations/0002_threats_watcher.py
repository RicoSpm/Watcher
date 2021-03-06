# Generated by Django 2.2.7 on 2019-12-18 09:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('threats_watcher', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trendyword',
            name='occurrences',
            field=models.IntegerField(default=1, help_text='Incremented by one when the same word is found in another post from RSS Feeds.'),
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('user_rec', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'subscribers',
            },
        ),
    ]
