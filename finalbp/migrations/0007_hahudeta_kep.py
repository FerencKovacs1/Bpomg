# Generated by Django 2.1.5 on 2019-03-18 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('finalbp', '0006_auto_20190318_1647'),
    ]

    operations = [
        migrations.AddField(
            model_name='hahudeta',
            name='kep',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='finalbp.Hahuautok'),
        ),
    ]
