# Generated by Django 4.0.1 on 2022-01-21 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('primecareapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='p_staff',
            old_name='confirm_Password',
            new_name='confirm_password',
        ),
    ]
