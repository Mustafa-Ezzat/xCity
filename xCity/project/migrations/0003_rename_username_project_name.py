# Generated by Django 5.0.6 on 2024-08-11 23:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_rename_developer_id_project_developer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='username',
            new_name='name',
        ),
    ]
