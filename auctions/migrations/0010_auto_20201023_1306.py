# Generated by Django 3.1.2 on 2020-10-23 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0009_auto_20201020_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='id',
            field=models.CharField(default='koOZZRyCyOmPUbJYKLNJjZfRQPQQtCYsCAbnjxqffPmiyafQJSSYsLIykORHYduiRzRvTK', max_length=150, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.CharField(default='ikGGFTupvPjLmizlUhVyIHnzqzRzYogOegpbVMAGqPZrsJKUdROSyQSdRCNIZysxApYcCV', max_length=150, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='comment',
            name='id',
            field=models.CharField(default='XjEyEtWodryqxtwezvDzYVukeEhdrkHHQIqeGHLAlgOSqSCRoqoaPOYzjUAFDeHwurrRIp', max_length=30, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='listing',
            name='id',
            field=models.CharField(default='DCFnEnkBRgZpDNyqptopQxNEBiaetIfiCqCdOUSpBbtZghduvGUYRFfhLkjdOFEQDEBYZE', max_length=150, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='watch',
            name='id',
            field=models.CharField(default='dnkTKHSnUcvwvKRxUmkFOOVRFxfpSYjVOMZSWYIYjrQVTSKyVSrFkWmHDlNOKYfAYquhzf', max_length=150, primary_key=True, serialize=False),
        ),
    ]
