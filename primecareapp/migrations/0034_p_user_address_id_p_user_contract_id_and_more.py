# Generated by Django 4.0.1 on 2022-02-02 09:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('primecareapp', '0033_p_user_otp'),
    ]

    operations = [
        migrations.AddField(
            model_name='p_user',
            name='Address_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='primecareapp.p_address'),
        ),
        migrations.AddField(
            model_name='p_user',
            name='Contract_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='primecareapp.p_contract'),
        ),
        migrations.AddField(
            model_name='p_user',
            name='Covid_test_expire_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='p_user',
            name='Covidteststatus',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='p_user',
            name='Experience_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='primecareapp.p_experience'),
        ),
        migrations.AddField(
            model_name='p_user',
            name='Handbook_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='primecareapp.p_handbook'),
        ),
        migrations.AddField(
            model_name='p_user',
            name='Insurance_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='primecareapp.p_insurance'),
        ),
        migrations.AddField(
            model_name='p_user',
            name='Photo_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='primecareapp.p_photo'),
        ),
        migrations.AddField(
            model_name='p_user',
            name='Pvg_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='primecareapp.p_pvg'),
        ),
        migrations.AddField(
            model_name='p_user',
            name='Qualification_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='primecareapp.p_qualification'),
        ),
        migrations.AddField(
            model_name='p_user',
            name='SortCode',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='p_user',
            name='Sssc_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='primecareapp.p_sssc'),
        ),
        migrations.AddField(
            model_name='p_user',
            name='Vaccination_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='primecareapp.p_vaccination_certificate'),
        ),
        migrations.AddField(
            model_name='p_user',
            name='Workpermit_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='primecareapp.p_work_permit_certificate'),
        ),
        migrations.AddField(
            model_name='p_user',
            name='skills',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='p_user',
            name='toc',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.DeleteModel(
            name='P_details',
        ),
    ]