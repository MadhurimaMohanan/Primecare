# Generated by Django 4.0.1 on 2022-02-05 07:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('primecareapp', '0042_p_caretaker'),
    ]

    operations = [
        migrations.RenameField(
            model_name='p_caretaker',
            old_name='message',
            new_name='description',
        ),
    ]
