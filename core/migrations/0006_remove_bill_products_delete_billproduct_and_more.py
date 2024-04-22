# Generated by Django 5.0.4 on 2024-04-22 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_billproduct_alter_bill_products'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bill',
            name='products',
        ),
        migrations.DeleteModel(
            name='billproduct',
        ),
        migrations.AddField(
            model_name='bill',
            name='products',
            field=models.JSONField(default={'sample': 'product'}),
            preserve_default=False,
        ),
    ]
