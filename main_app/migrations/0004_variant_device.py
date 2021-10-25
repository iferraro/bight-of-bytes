# Generated by Django 3.0 on 2021-10-25 22:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_remove_variant_device'),
    ]

    operations = [
        migrations.AddField(
            model_name='variant',
            name='device',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='main_app.Device'),
            preserve_default=False,
        ),
    ]