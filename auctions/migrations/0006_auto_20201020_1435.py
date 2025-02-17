# Generated by Django 3.1.2 on 2020-10-20 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_auto_20201020_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='id',
            field=models.CharField(default='qKubQqMJEkpPssJMJLgmpCxwOTBRQkMEvxMaaMdDDlHOHaqvEWrXCHqyBnyHTnjHPDFcro', max_length=150, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.CharField(default='nOnivHTRGgtAaLyGRZKSTqErFPBvbAUHYnKOOvMWXoEutZVsnAJWlOpBYxRWYlJTFjjsle', max_length=150, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='comment',
            name='id',
            field=models.CharField(default='fgzXyQFSkjhWKyIAAGHmonBwfckCqxcyEBDkULimIOaahveRzpNvhKzohTEfDWIUvXuCVA', max_length=30, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='listing',
            name='id',
            field=models.CharField(default='ZvvBGDxVqpmaDVQlkLLbcOcGDQFBUYqzBdVUCUflUSIXNnMZjESIyBfJqivGAcpjxprcTs', max_length=150, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='watch',
            name='id',
            field=models.CharField(default='QHHWyycyHjiMjJgUYwKzZekmdYoAuzzFPagmXXHkzSBJybQxfwSEloJtXKJTPfeEyLaNpu', max_length=150, primary_key=True, serialize=False),
        ),
    ]
