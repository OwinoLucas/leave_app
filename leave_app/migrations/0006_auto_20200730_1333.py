# Generated by Django 3.0.8 on 2020-07-30 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leave_app', '0005_auto_20200730_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='id_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
