# Generated by Django 5.0.4 on 2024-05-12 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_salarymanagement_withdrawal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='salarymanagement',
            name='withdrawal',
        ),
        migrations.AddField(
            model_name='salarymanagement',
            name='transaction',
            field=models.JSONField(default={'Data': None}),
            preserve_default=False,
        ),
    ]
