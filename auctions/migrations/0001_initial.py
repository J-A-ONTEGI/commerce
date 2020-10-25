# Generated by Django 3.1.2 on 2020-10-17 18:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=90, unique=True, verbose_name='email')),
                ('username', models.CharField(max_length=30, primary_key=True, serialize=False, verbose_name='username')),
                ('first_name', models.CharField(max_length=30, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=30, verbose_name='Last Name')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('name', models.CharField(blank=True, max_length=20, null=True)),
                ('id', models.CharField(default='kRMsdeeSAXqNqVjPBKCHDXEJYQwGnjydlccFPXnWwXOcrUSVWoPYpRpXAJzTqjqsjOmpDH', max_length=150, primary_key=True, serialize=False)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auctions.category')),
            ],
        ),
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.CharField(default='bfMLkbxEbeQlVNttpYrroRzfkXAvulKyUZWMhypUpBrgtgcTGJHQUaupkfANeQRbRFfiHO', max_length=150, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('starting_bid', models.FloatField(blank=True, null=True)),
                ('description', models.TextField(blank=True, max_length=1000, null=True)),
                ('img_url', models.URLField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('category', models.ManyToManyField(to='auctions.Category')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users_listings', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Watch',
            fields=[
                ('id', models.CharField(default='WDxEEwPKgwHaIGaesKEHHzYtjPaENTFAQLlwmEkgeqJBCzsSqYCasaiVEVcStUBQORQJox', max_length=150, primary_key=True, serialize=False)),
                ('listing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='watched', to='auctions.listing')),
                ('watcher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='watcher', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.CharField(default='kVCaXADGQsTqfImVwZsMmbHuiKdEnGQltacNPYpgNAxhtUROEslHTLrCDRrcOZorHRtGme', max_length=30, primary_key=True, serialize=False)),
                ('content', models.TextField(blank=True, null=True)),
                ('made_on', models.DateTimeField(auto_now=True)),
                ('listing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auctions.listing')),
                ('poster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auctions.customuser')),
                ('prev_login', models.DateTimeField(auto_now_add=True)),
                ('watchlist', models.ManyToManyField(null=True, to='auctions.Watch')),
            ],
        ),
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.CharField(default='pWhvTMIcPVJogPznZIZUvBWHYicmtOknvTfMhoFyBQApowgnlMtnnOQgTYfWZQbnuYtDbj', max_length=150, primary_key=True, serialize=False)),
                ('bid_date', models.DateTimeField(auto_now_add=True)),
                ('price', models.FloatField(blank=True, null=True)),
                ('is_winning_bid', models.BooleanField(default=False)),
                ('listing', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auctions.listing')),
                ('bidder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auctions.profile')),
            ],
        ),
    ]
