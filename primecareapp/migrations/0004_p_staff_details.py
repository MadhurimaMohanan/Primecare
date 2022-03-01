# Generated by Django 4.0.1 on 2022-01-22 05:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('primecareapp', '0003_p_staff_toc'),
    ]

    operations = [
        migrations.CreateModel(
            name='P_Staff_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(default='', max_length=100)),
                ('phone_number', models.CharField(default='', max_length=100)),
                ('email', models.CharField(default='', max_length=100)),
                ('sort_code', models.CharField(default='', max_length=100)),
                ('photo', models.ImageField(default='', upload_to='photo')),
                ('covid_test_status', models.CharField(default='', max_length=100)),
                ('covid_test_expire_date', models.CharField(default='', max_length=100)),
                ('vaccine_certificate', models.FileField(default='', upload_to='vaccine-certificate')),
                ('work_permit', models.FileField(default='', upload_to='work-permit')),
                ('address_proof', models.FileField(default='', upload_to='address-proof')),
                ('insurance', models.FileField(default='', upload_to='insurance')),
                ('sssc', models.FileField(default='', upload_to='sssc')),
                ('skills', models.CharField(default='', max_length=100)),
                ('pvg', models.FileField(default='', upload_to='pvg')),
                ('qualification', models.FileField(default='', upload_to='qualification')),
                ('handbook', models.FileField(default='', upload_to='handbook')),
                ('contract', models.FileField(default='', upload_to='contract')),
                ('experience', models.FileField(default='', upload_to='experience')),
                ('P_Staff_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='primecareapp.p_staff')),
            ],
        ),
    ]