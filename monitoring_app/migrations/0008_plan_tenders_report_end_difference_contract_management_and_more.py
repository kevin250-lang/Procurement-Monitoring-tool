# Generated by Django 5.0 on 2024-10-31 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring_app', '0007_plan_tenders_report_actual_contract_management_end_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan_tenders_report',
            name='end_difference_contract_management',
            field=models.DurationField(null=True),
        ),
        migrations.AddField(
            model_name='plan_tenders_report',
            name='end_difference_contract_signing',
            field=models.DurationField(null=True),
        ),
        migrations.AddField(
            model_name='plan_tenders_report',
            name='end_difference_evaluation',
            field=models.DurationField(null=True),
        ),
        migrations.AddField(
            model_name='plan_tenders_report',
            name='end_difference_final_notification',
            field=models.DurationField(null=True),
        ),
        migrations.AddField(
            model_name='plan_tenders_report',
            name='end_difference_opening_date',
            field=models.DurationField(null=True),
        ),
        migrations.AddField(
            model_name='plan_tenders_report',
            name='end_difference_provisional_notification',
            field=models.DurationField(null=True),
        ),
        migrations.AddField(
            model_name='plan_tenders_report',
            name='end_difference_publication_date',
            field=models.DurationField(null=True),
        ),
        migrations.AddField(
            model_name='plan_tenders_report',
            name='end_difference_tender_doc_preparation',
            field=models.DurationField(null=True),
        ),
        migrations.AddField(
            model_name='plan_tenders_report',
            name='start_difference_contract_management',
            field=models.DurationField(null=True),
        ),
        migrations.AddField(
            model_name='plan_tenders_report',
            name='start_difference_contract_signing',
            field=models.DurationField(null=True),
        ),
        migrations.AddField(
            model_name='plan_tenders_report',
            name='start_difference_evaluation',
            field=models.DurationField(null=True),
        ),
        migrations.AddField(
            model_name='plan_tenders_report',
            name='start_difference_final_notification',
            field=models.DurationField(null=True),
        ),
        migrations.AddField(
            model_name='plan_tenders_report',
            name='start_difference_opening_date',
            field=models.DurationField(null=True),
        ),
        migrations.AddField(
            model_name='plan_tenders_report',
            name='start_difference_provisional_notification',
            field=models.DurationField(null=True),
        ),
        migrations.AddField(
            model_name='plan_tenders_report',
            name='start_difference_publication_date',
            field=models.DurationField(null=True),
        ),
        migrations.AddField(
            model_name='plan_tenders_report',
            name='start_difference_tender_doc_preparation',
            field=models.DurationField(null=True),
        ),
    ]
