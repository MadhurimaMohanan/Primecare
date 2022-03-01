# Generated by Django 3.1.4 on 2022-02-19 07:55

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('primecareapp', '0051_remove_p_user_select'),
    ]

    operations = [
        migrations.CreateModel(
            name='P_previous_employer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('employername1', models.CharField(default='', max_length=100, null=True)),
                ('telenum1', models.CharField(default='', max_length=100, null=True)),
                ('employermail1', models.CharField(default='', max_length=100, null=True)),
                ('address1', models.CharField(default='', max_length=100, null=True)),
                ('employername2', models.CharField(default='', max_length=100, null=True)),
                ('telenum2', models.CharField(default='', max_length=100, null=True)),
                ('employermail2', models.CharField(default='', max_length=100, null=True)),
                ('address2', models.CharField(default='', max_length=100, null=True)),
                ('payslip1', models.FileField(default='', null=True, upload_to='payslip1')),
                ('payslip2', models.FileField(default='', null=True, upload_to='payslip2')),
            ],
        ),
        migrations.RenameField(
            model_name='p_work_permit_certificate',
            old_name='expiry_date',
            new_name='brp_expiry_date',
        ),
        migrations.RemoveField(
            model_name='p_work_permit_certificate',
            name='Permit',
        ),
        migrations.AddField(
            model_name='p_work_permit_certificate',
            name='brp',
            field=models.FileField(default='', null=True, upload_to='brp'),
        ),
        migrations.AddField(
            model_name='p_work_permit_certificate',
            name='passport',
            field=models.FileField(default='', null=True, upload_to='passport'),
        ),
        migrations.AddField(
            model_name='p_work_permit_certificate',
            name='passport_expiry_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='p_work_permit_certificate',
            name='visa',
            field=models.FileField(default='', null=True, upload_to='visa'),
        ),
        migrations.AddField(
            model_name='p_work_permit_certificate',
            name='visa_expiry_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='p_user',
            name='Workpermit_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='primecareapp.p_work_permit_certificate'),
        ),
        migrations.AddField(
            model_name='p_user',
            name='Previous_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='primecareapp.p_previous_employer'),
        ),
    ]