# Generated by Django 3.0.8 on 2020-08-03 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leave_app', '0010_auto_20200803_1103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='department',
            field=models.CharField(choices=[('Operations', 'Operations'), ('Marketing & Sales', 'Marketing & Sales'), ('Programs', 'Programs'), ('Editorial', 'Editorial'), ('Technical', 'Technical'), ('Digital', 'Digital'), ('Graphics', 'Graphics'), ('Innovations', 'Innovations'), ('Bureau Heads', 'Bureau Heads'), ('C.E.O', 'C.E.O')], max_length=70, null=True),
        ),
    ]