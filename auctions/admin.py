from django.contrib import admin
from .models import CustomUser, Bid, Category, Comment, Listing, Watch, Profile


# Register your models here.


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_admin', 'is_superuser')


class BidAdmin(admin.ModelAdmin):
    list_display = ('id', 'price')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'content')


class ListingAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'starting_bid', 'is_active')


class WatchAdmin(admin.ModelAdmin):
    list_display = ('watcher_name', 'listing_id')


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Bid, BidAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Listing, ListingAdmin)
admin.site.register(Watch, WatchAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Profile)
