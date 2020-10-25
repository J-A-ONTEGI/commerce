from django.urls import path

from . import views

app_name = 'auctions'

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("listing/<str:listing_id>", views.listing, name="listing"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("category/<str:category_id>", views.category, name="category"),
    path("addlisting", views.create_listing, name="createlisting"),
    path("bid/<str:listing_id>", views.bid, name="bid"),
    path("close", views.end_bidding, name="close"),
    path("watch/<str:listing_id>", views.watch, name="add-to-watchlist"),
    path("unwatch/<str:listing_id>", views.unwatch, name="remove-from-watchlist"),
    path("mylistings", views.my_listings, name="my_listings"),
    path("comment/<str:listing_id>", views.comment, name="comment"),
    path("categories", views.categories, name="categories"),
    path("winnings", views.won, name="won"),
]
