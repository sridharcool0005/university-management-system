# Generated by Django 2.1 on 2018-10-02 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0020_auto_20181002_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feegroup',
            name='fee_types',
            field=models.ManyToManyField(to='students.FeeType'),
        ),
    ]
