# Generated by Django 3.0.8 on 2020-07-30 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leave_app', '0002_auto_20200730_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='gender',
            field=models.CharField(choices=[('Female', 'Female'), ('Male', 'Male')], max_length=7),
        ),
    ]
