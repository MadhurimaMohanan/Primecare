# Generated by Django 3.1.4 on 2022-02-21 07:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('primecareapp', '0053_remove_p_user_workpermit_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='p_user',
            name='Previous_id',
        ),
    ]
