# Generated by Django 4.0.1 on 2022-02-04 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('primecareapp', '0038_user_temp'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_temp',
            name='otp',
            field=models.CharField(default='', max_length=100),
        ),
    ]