# Generated by Django 4.0.1 on 2022-01-24 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('primecareapp', '0011_rename_document_p_sssc_certificate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='p_sssc',
            name='certificate',
            field=models.FileField(blank=True, default='', null=True, upload_to='sssc'),
        ),
    ]
