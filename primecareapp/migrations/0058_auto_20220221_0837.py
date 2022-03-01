# Generated by Django 3.1.4 on 2022-02-21 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('primecareapp', '0057_auto_20220221_0806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='p_previous_employer',
            name='address1',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='p_previous_employer',
            name='address2',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='p_previous_employer',
            name='employermail1',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='p_previous_employer',
            name='employermail2',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='p_previous_employer',
            name='employername1',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='p_previous_employer',
            name='employername2',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='p_previous_employer',
            name='telenum1',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='p_previous_employer',
            name='telenum2',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
    ]
