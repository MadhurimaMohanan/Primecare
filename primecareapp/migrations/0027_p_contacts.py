# Generated by Django 4.0.1 on 2022-01-27 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('primecareapp', '0026_rename_username_p_contact_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='P_Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='', max_length=100)),
                ('Email', models.CharField(default='', max_length=100)),
                ('Message', models.CharField(default='', max_length=100)),
            ],
        ),
    ]
