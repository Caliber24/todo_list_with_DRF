# Generated by Django 5.1.3 on 2024-12-03 13:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task_module', '0002_alter_task_is_completed'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='is_completed',
            new_name='is_complete',
        ),
    ]