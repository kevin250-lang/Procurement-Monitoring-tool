# Generated by Django 5.0 on 2024-10-24 13:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan_tenders_report',
            name='tender',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tender_report', to='monitoring_app.tender'),
        ),
        migrations.CreateModel(
            name='Tender_republished',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_id', models.CharField(max_length=50, null=True)),
                ('project_Name', models.CharField(max_length=50, null=True)),
                ('activity_sequence', models.IntegerField(null=True)),
                ('activity_id', models.CharField(max_length=80, null=True)),
                ('activity_description', models.CharField(max_length=250, null=True)),
                ('tender_count', models.IntegerField(null=True)),
                ('early_start', models.DateTimeField(null=True)),
                ('early_finish', models.DateTimeField(null=True)),
                ('total_work_days', models.IntegerField(null=True)),
                ('activity_status', models.CharField(max_length=80, null=True)),
                ('total_days', models.IntegerField(null=True)),
                ('elapsed_work_days', models.DecimalField(decimal_places=2, max_digits=19, null=True)),
                ('remaining_days', models.IntegerField(null=True)),
                ('remaining_work_days', models.DecimalField(decimal_places=2, max_digits=19, null=True)),
                ('note', models.CharField(blank=True, max_length=120, null=True)),
                ('actual_start', models.DateTimeField(null=True)),
                ('actual_finish', models.DateTimeField(null=True)),
                ('canceled', models.DateTimeField(null=True)),
                ('released_date', models.DateTimeField(null=True)),
                ('completed', models.DateTimeField(null=True)),
                ('closed', models.DateTimeField(null=True)),
                ('used', models.DateTimeField(null=True)),
                ('estimated_cost', models.IntegerField(null=True)),
                ('planned_cost', models.IntegerField(null=True)),
                ('baseline_cost', models.IntegerField(null=True)),
                ('planned_committed_cost', models.IntegerField(null=True)),
                ('committed_cost', models.IntegerField(null=True)),
                ('used_cost', models.IntegerField(null=True)),
                ('actual_cost', models.IntegerField(null=True)),
                ('set_in_baseline', models.CharField(blank=True, max_length=120, null=True)),
                ('baseline_revision_comment', models.CharField(blank=True, max_length=120, null=True)),
                ('activity_changed', models.BooleanField(default=False)),
                ('financially_responsible_id', models.CharField(blank=True, max_length=80, null=True)),
                ('financially_responsible_name', models.CharField(blank=True, max_length=80, null=True)),
                ('created', models.DateField(null=True)),
                ('responsible_id', models.IntegerField(null=True)),
                ('responsible_name', models.CharField(max_length=100, null=True)),
                ('activity_created_by', models.CharField(max_length=100, null=True)),
                ('modified', models.CharField(max_length=15, null=True)),
                ('modified_by', models.CharField(max_length=35, null=True)),
                ('activity_type', models.CharField(max_length=25, null=True)),
                ('source_of_fund', models.CharField(max_length=50, null=True)),
                ('planned_tender_doc_preparation', models.DateField(null=True)),
                ('planned_publication_date', models.DateField(null=True)),
                ('planned_bid_opening_date', models.DateField(null=True)),
                ('planned_start_evaluation', models.DateField(null=True)),
                ('planned_end_evaluation', models.DateField(null=True)),
                ('planned_provisional_notification_date', models.DateField(null=True)),
                ('planned_final_notification_date', models.DateField(null=True)),
                ('planned_contract_management_start_date', models.DateField(null=True)),
                ('planned_contract_signing_date', models.DateField(null=True)),
                ('planned_contract_end_date', models.DateField(null=True)),
                ('supervising_firm', models.BooleanField(default=False)),
                ('planned_budget', models.CharField(max_length=25, null=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tender_department', to='monitoring_app.department')),
                ('procurement_doc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='proc_document', to='monitoring_app.procurement_doc')),
                ('tender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='republished_tender', to='monitoring_app.tender')),
                ('tendering_method', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='monitoring_app.method')),
            ],
        ),
        migrations.AddField(
            model_name='plan_tenders_report',
            name='tender_republish',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='republished_tender_report', to='monitoring_app.tender_republished'),
        ),
    ]
