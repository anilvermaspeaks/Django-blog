# Generated by Django 4.1.5 on 2023-02-06 03:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='sug',
            new_name='slug',
        ),
    ]