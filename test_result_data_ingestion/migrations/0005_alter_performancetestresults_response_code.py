# Generated by Django 4.2.3 on 2023-07-30 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("test_result_data_ingestion", "0004_alter_performancetestresults_success"),
    ]

    operations = [
        migrations.AlterField(
            model_name="performancetestresults",
            name="response_code",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
