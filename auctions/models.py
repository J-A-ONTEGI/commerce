from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from .util import random_string


class UserManager(BaseUserManager):
    def create_user(self, username, email, first_name, last_name, password=None):
        if not email or not username or not first_name or not last_name:
            raise Exception(
                "Input Error: Ensure that all required Fields are correctly filled")
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,

        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, first_name, last_name, password=None, is_active=True, is_staff=True,
                         is_admin=True):
        if not email or not username or not first_name or not last_name:
            raise Exception(
                "Input Error: Ensure that all required Fields are correctly filled")
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
            is_active=is_active,
            is_staff=is_staff,
            is_admin=is_admin,
            is_superuser=True

        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staff(self, username, first_name, last_name, email, is_active=True, is_staff=True, password=None):
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
            is_active=is_active,
            is_staff=is_staff
        )
        user.set_password(password)
        user.save()
        return user


class CustomUser(AbstractBaseUser):
    email = models.EmailField(verbose_name='email', max_length=90, unique=True)
    username = models.CharField(verbose_name='username', max_length=30, primary_key=True)
    first_name = models.CharField(verbose_name='First Name', max_length=30, blank=False)
    last_name = models.CharField(verbose_name='Last Name', max_length=30, blank=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    objects = UserManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


class Category(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    id = models.CharField(primary_key=True, max_length=150, default=random_string(70))
    parent = models.ForeignKey("self", on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name


class Listing(models.Model):
    id = models.CharField(primary_key=True, max_length=150, default=random_string(70))
    name = models.CharField(max_length=30, null=True, blank=True)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='users_listings')
    starting_bid = models.FloatField(blank=True, null=True)
    description = models.TextField(max_length=1000, blank=True, null=True)
    img_url = models.URLField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    category = models.ManyToManyField(Category)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Watch(models.Model):
    id = models.CharField(primary_key=True, max_length=150, default=random_string(70))
    watcher_name = models.CharField(max_length=150)
    listing_id = models.CharField(null=True, max_length=150)
    listing_name = models.CharField(null=True, max_length=150)

    def __str__(self):
        return self.watcher_name


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, primary_key=True, on_delete=models.CASCADE)
    prev_login = models.DateTimeField(auto_now_add=True)
    watchlist = models.ManyToManyField(Watch)


class Bid(models.Model):
    id = models.CharField(primary_key=True, max_length=150, default=random_string(70))
    bidder = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    bid_date = models.DateTimeField(auto_now_add=True)
    price = models.FloatField(blank=True, null=True)
    is_winning_bid = models.BooleanField(default=False)


class Comment(models.Model):
    poster = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    id = models.CharField(primary_key=True, max_length=30, default=random_string(70))
    content = models.TextField(blank=True, null=True)
    made_on = models.DateTimeField(auto_now_add=True)
