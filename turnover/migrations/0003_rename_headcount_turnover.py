# Generated by Django 3.2.7 on 2024-02-02 19:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('turnover', '0002_rename_fg_dismissal_on_date_headcount_fg_dismissal_on_month'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Headcount',
            new_name='Turnover',
        ),
    ]
