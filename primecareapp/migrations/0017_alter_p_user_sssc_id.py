# Generated by Django 4.0.1 on 2022-01-25 04:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('primecareapp', '0016_p_sssc_expiry_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='p_user',
            name='Sssc_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='primecareapp.p_sssc'),
        ),
    ]