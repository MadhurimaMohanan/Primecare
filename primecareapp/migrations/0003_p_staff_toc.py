# Generated by Django 4.0.1 on 2022-01-21 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('primecareapp', '0002_rename_confirm_password_p_staff_confirm_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='p_staff',
            name='toc',
            field=models.CharField(default='', max_length=100),
        ),
    ]
