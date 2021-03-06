# Generated by Django 3.0.7 on 2021-07-14 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='acc_code',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Code', models.CharField(default=None, max_length=500)),
                ('Name', models.CharField(default=None, max_length=500)),
                ('Notes', models.TextField(default=None)),
                ('Flag', models.CharField(default=None, max_length=500)),
                ('Type', models.BooleanField(default=False, null=True)),
                ('Ekfal', models.CharField(default=None, max_length=500, null=True)),
                ('Normal', models.CharField(default=None, max_length=500, null=True)),
                ('Level', models.CharField(default=None, max_length=500, null=True)),
                ('Mem_Volume_M', models.CharField(default=None, max_length=500, null=True)),
                ('Mem_Volume_W', models.CharField(default=None, max_length=500, null=True)),
                ('Mem_Volume', models.CharField(default=None, max_length=500, null=True)),
                ('Mem_City', models.CharField(default=None, max_length=500, null=True)),
                ('Mem_Count', models.CharField(default=None, max_length=500, null=True)),
                ('Mem_Tel', models.CharField(default=None, max_length=500, null=True)),
                ('Mem_Address', models.TextField(default=None, null=True)),
                ('Mem_Pay', models.BooleanField(default=False, null=True)),
                ('Mem_LDate', models.CharField(default=None, max_length=500, null=True)),
            ],
            options={
                'db_table': 'acc_code',
            },
        ),
    ]
