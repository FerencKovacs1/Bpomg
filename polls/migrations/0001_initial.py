# Generated by Django 2.1.5 on 2019-03-13 23:38

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vezeteknev', models.CharField(max_length=50)),
                ('keresztnev', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=70, null=True, unique=True)),
                ('phone', phone_field.models.PhoneField(blank=True, help_text='Amin eltudjuk érni', max_length=31)),
                ('gepkocsimarkaja', models.CharField(help_text='Példa: Opel', max_length=50)),
                ('gepkocsitipus', models.CharField(help_text='Példa: Astra', max_length=50)),
                ('gepkocsirendszama', models.CharField(help_text='Példa: AAA - 111', max_length=6)),
                ('uzenet', models.TextField()),
            ],
        ),
    ]