# Generated by Django 2.1.5 on 2019-04-28 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finalbp', '0005_hahudeta_ar'),
    ]

    operations = [
        migrations.AddField(
            model_name='hahudeta',
            name='allapot',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='hahudeta',
            name='email',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='hahudeta',
            name='hengerelrendezes',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='hahudeta',
            name='muszaki',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='hahudeta',
            name='sebessegvalto',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='hahudeta',
            name='szin',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='hahudeta',
            name='teljesitmeny',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
