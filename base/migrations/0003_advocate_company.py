# Generated by Django 5.0.4 on 2024-05-12 07:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='advocate',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.company'),
        ),
    ]
