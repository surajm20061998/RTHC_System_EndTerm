# Generated by Django 5.1.3 on 2024-11-23 01:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alert',
            fields=[
                ('alert_id', models.AutoField(primary_key=True, serialize=False)),
                ('timestamp', models.DateTimeField()),
                ('alert_type', models.CharField(max_length=100)),
                ('severity', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('status', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'alert',
            },
        ),
        migrations.CreateModel(
            name='DeviceType',
            fields=[
                ('deviceType_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('manufacturer', models.CharField(max_length=255)),
                ('model_series', models.CharField(max_length=255)),
                ('monitoring_capabilities', models.TextField()),
            ],
            options={
                'db_table': 'devicetype',
            },
        ),
        migrations.CreateModel(
            name='PatientMonitor',
            fields=[
                ('monitor_id', models.AutoField(primary_key=True, serialize=False)),
                ('serial_number', models.CharField(max_length=255, unique=True)),
                ('manufacturer', models.CharField(max_length=255)),
                ('model_number', models.CharField(max_length=255)),
                ('last_maintenance_date', models.DateField(blank=True, null=True)),
                ('calibration_date', models.DateField(blank=True, null=True)),
                ('status', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'patientmonitor',
            },
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('staff_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('ssn', models.CharField(max_length=20, unique=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=50)),
                ('role', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=100)),
                ('hire_date', models.DateField(blank=True, null=True)),
                ('license_number', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'staff',
            },
        ),
        migrations.CreateModel(
            name='VitalRecord',
            fields=[
                ('record_id', models.AutoField(primary_key=True, serialize=False)),
                ('timestamp', models.DateTimeField()),
                ('heart_rate', models.IntegerField(blank=True, null=True)),
                ('blood_pressure_systolic', models.IntegerField(blank=True, null=True)),
                ('blood_pressure_diastolic', models.IntegerField(blank=True, null=True)),
                ('temperature', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('respiratory_rate', models.IntegerField(blank=True, null=True)),
                ('oxygen_saturation', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'vitalrecords',
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('patient_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('ssn', models.CharField(max_length=20, unique=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(max_length=20)),
                ('blood_type', models.CharField(max_length=5)),
                ('admission_date', models.DateField(blank=True, null=True)),
                ('discharge_date', models.DateField(blank=True, null=True)),
                ('status', models.CharField(max_length=50)),
                ('primary_physician', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='patients', to='dashboard.staff')),
            ],
            options={
                'db_table': 'patient',
            },
        ),
        migrations.CreateModel(
            name='AlertRequiresAction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('required_action_type', models.CharField(max_length=100)),
                ('required_response_time', models.IntegerField()),
                ('priority_level', models.CharField(max_length=50)),
                ('escalation_threshold', models.IntegerField()),
                ('alert', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.alert')),
            ],
            options={
                'db_table': 'alert_requires_action',
                'unique_together': {('alert', 'required_action_type')},
            },
        ),
        migrations.CreateModel(
            name='PatientMonitorAssignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assignment_date', models.DateTimeField()),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('monitoring_protocol_id', models.CharField(max_length=255)),
                ('monitor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.patientmonitor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.patient')),
                ('assigned_by_staff', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.staff')),
            ],
            options={
                'db_table': 'patientmonitorassignment',
                'unique_together': {('patient', 'monitor', 'assignment_date')},
            },
        ),
        migrations.CreateModel(
            name='DeviceTypeDefinesMonitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('definition_date', models.DateField(blank=True, null=True)),
                ('device_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.devicetype')),
                ('monitor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.patientmonitor')),
                ('configured_by_staff', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.staff')),
            ],
            options={
                'db_table': 'devicetype_defines_monitor',
                'unique_together': {('device_type', 'monitor')},
            },
        ),
        migrations.CreateModel(
            name='StaffHandlesPatient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assignment_start_date', models.DateField()),
                ('assignment_end_date', models.DateField(blank=True, null=True)),
                ('care_role', models.CharField(max_length=100)),
                ('shift_schedule', models.CharField(max_length=100)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.patient')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.staff')),
            ],
            options={
                'db_table': 'staff_handles_patient',
                'unique_together': {('staff', 'patient', 'assignment_start_date')},
            },
        ),
        migrations.CreateModel(
            name='StaffTakesAction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_timestamp', models.DateTimeField()),
                ('action_taken', models.TextField()),
                ('response_time', models.IntegerField()),
                ('follow_up_required', models.BooleanField()),
                ('alert', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.alert')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.staff')),
            ],
            options={
                'db_table': 'staff_takes_action',
                'unique_together': {('staff', 'alert', 'action_timestamp')},
            },
        ),
        migrations.CreateModel(
            name='PatientHasVitalRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recording_session_id', models.CharField(max_length=255)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.patient')),
                ('recorded_by_staff', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.staff')),
                ('vital_record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.vitalrecord')),
            ],
            options={
                'db_table': 'patient_has_vitalrecords',
                'unique_together': {('patient', 'vital_record')},
            },
        ),
        migrations.CreateModel(
            name='MonitorRecordsVital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recording_start_time', models.DateTimeField(blank=True, null=True)),
                ('recording_end_time', models.DateTimeField(blank=True, null=True)),
                ('data_quality_score', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('monitor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.patientmonitor')),
                ('vital_record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.vitalrecord')),
            ],
            options={
                'db_table': 'monitor_records_vitals',
                'unique_together': {('monitor', 'vital_record')},
            },
        ),
        migrations.CreateModel(
            name='VitalRecordTriggersAlert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trigger_threshold_value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('trigger_condition', models.CharField(max_length=255)),
                ('trigger_timestamp', models.DateTimeField()),
                ('alert', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.alert')),
                ('vital_record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.vitalrecord')),
            ],
            options={
                'db_table': 'vitalrecords_triggers_alert',
                'unique_together': {('vital_record', 'alert')},
            },
        ),
    ]