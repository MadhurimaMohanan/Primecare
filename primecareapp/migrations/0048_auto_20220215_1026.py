# Generated by Django 3.1.4 on 2022-02-15 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('primecareapp', '0047_auto_20220215_0441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='p_user',
            name='Workpermit_id',
            field=models.CharField(default='', max_length=100),
        ),
    ]
