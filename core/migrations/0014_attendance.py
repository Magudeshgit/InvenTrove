# Generated by Django 5.0.4 on 2024-04-26 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_remove_bill_billno'),
    ]

    operations = [
        migrations.CreateModel(
            name='attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('absentees', models.ManyToManyField(to='core.labor')),
            ],
        ),
    ]
