# Generated by Django 4.0.1 on 2022-02-03 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('primecareapp', '0035_alter_p_address_proof_alter_p_contract_contract_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='p_user',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]