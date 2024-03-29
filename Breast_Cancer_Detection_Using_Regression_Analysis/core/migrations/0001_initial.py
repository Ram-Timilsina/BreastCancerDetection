# Generated by Django 4.2.3 on 2023-08-01 04:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BreastCancerData',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('radius_mean', models.FloatField()),
                ('texture_mean', models.FloatField()),
                ('perimeter_mean', models.FloatField()),
                ('area_mean', models.FloatField()),
                ('smoothness_mean', models.FloatField()),
                ('compactness_mean', models.FloatField()),
                ('concavity_mean', models.FloatField()),
                ('concave_points_mean', models.FloatField()),
                ('symmetry_mean', models.FloatField()),
                ('fractal_dimension_mean', models.FloatField()),
                ('radius_se', models.FloatField()),
                ('texture_se', models.FloatField()),
                ('perimeter_se', models.FloatField()),
                ('area_se', models.FloatField()),
                ('smoothness_se', models.FloatField()),
                ('compactness_se', models.FloatField()),
                ('concavity_se', models.FloatField()),
                ('concave_points_se', models.FloatField()),
                ('symmetry_se', models.FloatField()),
                ('fractal_dimension_se', models.FloatField()),
                ('radius_worst', models.FloatField()),
                ('texture_worst', models.FloatField()),
                ('perimeter_worst', models.FloatField()),
                ('area_worst', models.FloatField()),
                ('smoothness_worst', models.FloatField()),
                ('compactness_worst', models.FloatField()),
                ('concavity_worst', models.FloatField()),
                ('concave_points_worst', models.FloatField()),
                ('symmetry_worst', models.FloatField()),
                ('fractal_dimension_worst', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='BreastScanTestResult',
            fields=[
                ('test_id', models.AutoField(primary_key=True, serialize=False)),
                ('test_type', models.CharField(max_length=100)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('Did', models.CharField(max_length=10, unique=True)),
                ('speciality', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('patient_id', models.AutoField(primary_key=True, serialize=False)),
                ('most_likely_diagnosis', models.CharField(max_length=100)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='PatientDoctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prescribed_test', models.CharField(max_length=100)),
                ('test_date', models.DateField()),
                ('Did', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.doctor')),
                ('Pid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.patient')),
            ],
        ),
        migrations.CreateModel(
            name='PatientBreastScan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_status', models.CharField(default=None, max_length=100)),
                ('Did', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.doctor')),
                ('Pid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.patient')),
                ('breast_attributes', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.breastcancerdata')),
                ('test_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.breastscantestresult')),
            ],
        ),
        migrations.AddField(
            model_name='breastscantestresult',
            name='Did',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.doctor'),
        ),
        migrations.AddField(
            model_name='breastscantestresult',
            name='Pid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.patient'),
        ),
    ]
