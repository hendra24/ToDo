# Generated by Django 4.2 on 2023-12-10 06:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='todo_list',
            new_name='task',
        ),
    ]
