# Generated by Django 4.0.1 on 2022-01-27 07:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('primecareapp', '0029_rename_covidtest_expire_date_p_user_covid_test_expire_date'),
    ]

    operations = [
        migrations.DeleteModel(
            name='P_Contacts',
        ),
    ]
