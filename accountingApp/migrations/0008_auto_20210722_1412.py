# Generated by Django 3.0.7 on 2021-07-22 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountingApp', '0007_transaction_notes'),
    ]

    operations = [
        migrations.AddField(
            model_name='acc_code_with_details',
            name='deleted',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='deleted',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
