# Generated by Django 3.1.2 on 2020-10-20 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_auto_20201020_1407'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='watch',
            name='listing',
        ),
        migrations.AddField(
            model_name='watch',
            name='listing_id',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='bid',
            name='id',
            field=models.CharField(default='XnCnusGsWvDdMNlyWjzpCHSEGzPCqheaNHAncPOArMeFkSIMuhwCigLUuzilNgzVPSTImY', max_length=150, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.CharField(default='MUPDjLBvZMwHOIvbGyKWropweCRkoOqmqibGYIvYjwtsbmcGiSNWGIiFpUgFUcNAtjLgrl', max_length=150, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='comment',
            name='id',
            field=models.CharField(default='ZtynoGdOBgBxnCXgdcdNqdzHXIrykFYAwSoRKOQOKCwcxxCsmbNQdjdpFVaioYUUlAJVIY', max_length=30, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='listing',
            name='id',
            field=models.CharField(default='BUQUzKbLSzlehtEYuztpRALCFuiREBJTYbrFaxzDNXtTicKcqwVSvKjnTCdGcduYqaVWDD', max_length=150, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='watch',
            name='id',
            field=models.CharField(default='pONhKFwIFaITNVVasyHQPwmDzyXSamyRsDoeQvdhjLDdhbYnISZCmXOSBNXOTAkzavBjQK', max_length=150, primary_key=True, serialize=False),
        ),
    ]
