# Generated by Django 2.1.7 on 2019-03-15 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listman', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='title',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='title',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]