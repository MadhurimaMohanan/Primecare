# Generated by Django 4.0.1 on 2022-01-24 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('primecareapp', '0013_alter_p_sssc_expiry_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='p_sssc',
            name='expiry_date',
            field=models.DateField(),
        ),
    ]