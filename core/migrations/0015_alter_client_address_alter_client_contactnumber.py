# Generated by Django 5.0.4 on 2024-04-26 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_attendance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='address',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='contactnumber',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
