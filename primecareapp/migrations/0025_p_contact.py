# Generated by Django 4.0.1 on 2022-01-25 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('primecareapp', '0024_remove_p_user_covidtest_expire_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='P_contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(default='', max_length=100)),
                ('Email', models.CharField(default='', max_length=100)),
                ('Message', models.CharField(default='', max_length=100)),
            ],
        ),
    ]
