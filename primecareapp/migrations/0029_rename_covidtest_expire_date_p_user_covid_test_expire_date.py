# Generated by Django 4.0.1 on 2022-01-27 06:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('primecareapp', '0028_p_user_covidtest_expire_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='p_user',
            old_name='Covidtest_expire_date',
            new_name='Covid_test_expire_date',
        ),
    ]