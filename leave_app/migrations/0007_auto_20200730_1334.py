# Generated by Django 3.0.8 on 2020-07-30 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leave_app', '0006_auto_20200730_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='date_of_employment',
            field=models.DateTimeField(null=True),
        ),
    ]