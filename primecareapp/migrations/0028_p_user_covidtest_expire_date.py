# Generated by Django 4.0.1 on 2022-01-27 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('primecareapp', '0027_p_contacts'),
    ]

    operations = [
        migrations.AddField(
            model_name='p_user',
            name='Covidtest_expire_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
