# Generated by Django 2.0.5 on 2018-05-16 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20180516_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='completionDate',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='dueDate',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
