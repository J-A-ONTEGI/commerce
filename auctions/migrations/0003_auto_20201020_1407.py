# Generated by Django 3.1.2 on 2020-10-20 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_auto_20201020_0928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='id',
            field=models.CharField(default='XIQHVGPhzwffjDIcnmaCHSccrCBDHilLGVPEgIbeTkLdGqSCWJOQYQELotWMNErwINPZXc', max_length=150, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.CharField(default='LGDJrcnaypSlRLcSeESFttZKDVoAXMNxVJfIKEHbjsstyenEIWaddWoxxxrHMzblIbheaS', max_length=150, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='comment',
            name='id',
            field=models.CharField(default='HlwwyPgGLiWVbDeYhgNcPjNjQqaBxnOcwQjKjjQLVJgHFPuTiiGCBmORbtmOFGISiMsyLX', max_length=30, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='listing',
            name='id',
            field=models.CharField(default='eykpUNSVkAHqYUfactWZwENLtslfIYUbHdiiYGTvmXRwcJbeaZlHNtzwFwxItKBtIJQgLy', max_length=150, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='watch',
            name='id',
            field=models.CharField(default='ocvbluvPrMprHOQGozbJbjsDRlZBqIpQFeArbPqmeHJplrxCFxQHsSssQYDGjbHBhweGIQ', max_length=150, primary_key=True, serialize=False),
        ),
    ]
