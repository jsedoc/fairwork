# Generated by Django 2.0.5 on 2018-07-25 04:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auditor', '0005_auto_20180724_2129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hit',
            name='hit_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auditor.HITType'),
        ),
    ]
