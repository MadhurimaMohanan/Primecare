# Generated by Django 4.0.1 on 2022-01-25 06:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('primecareapp', '0023_rename_covid_test_expire_date_p_user_covidtest_expire_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='p_user',
            name='Covidtest_expire_date',
        ),
    ]
