# Generated by Django 3.0.7 on 2021-07-14 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountingApp', '0002_auto_20210715_0029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acc_code',
            name='Notes',
            field=models.TextField(default=None, null=True),
        ),
    ]
