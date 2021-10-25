# Generated by Django 3.2.6 on 2021-10-25 20:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='device',
            name='variants',
        ),
        migrations.AddField(
            model_name='variant',
            name='device',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='main_app.device'),
            preserve_default=False,
        ),
    ]
