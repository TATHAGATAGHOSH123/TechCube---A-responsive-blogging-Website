# Generated by Django 3.2.6 on 2021-08-18 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='name',
        ),
        migrations.AddField(
            model_name='contact',
            name='fname',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='contact',
            name='lname',
            field=models.CharField(default='', max_length=50),
        ),
    ]
