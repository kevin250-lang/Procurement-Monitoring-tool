# Generated by Django 5.0 on 2024-10-28 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring_app', '0004_overall_department_republished_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan_tenders_report',
            name='removed',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='tender',
            name='removed',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='tender_republished',
            name='removed',
            field=models.DateTimeField(null=True),
        ),
    ]
