# Generated by Django 4.0.1 on 2022-01-25 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('primecareapp', '0019_alter_p_user_covid_test_expire_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='p_user',
            name='Covid_test_expire_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
