# Generated by Django 3.2.10 on 2023-12-02 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_todo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='title',
            field=models.TextField(max_length=255),
        ),
    ]