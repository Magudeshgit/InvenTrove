# Generated by Django 5.0.4 on 2024-04-26 12:32

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_rename_grandtotal_bill_billno_remove_bill_billdate_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='billdate',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bill',
            name='billstatus',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='bill',
            name='client',
            field=models.ForeignKey(blank=True, default=4, on_delete=django.db.models.deletion.CASCADE, to='core.client'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bill',
            name='grandtotal',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='bill',
            name='products',
            field=models.JSONField(blank=True, default={'example': 2}),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bill',
            name='billno',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
