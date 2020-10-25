from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import AddCategoryForm, AddCommentForm, AddListingForm
from .models import CustomUser, Bid, Listing, Category, Comment, Watch, Profile
from django.contrib.auth.decorators import login_required
from .util import random_string


def index(request):
    if request.user.is_authenticated:
        context = {
            'listings': Listing.objects.all().filter(is_active=True).exclude(owner=request.user)
        }
        return render(request, 'auctions/index.html', context)

    else:
        listings = Listing.objects.all().filter(is_active=True)
        return render(request, 'auctions/index.html', {
            'listings': Listing.objects.filter(is_active=True)
        })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("auctions:index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("auctions:index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = CustomUser.objects.create_user(username, email, first_name, last_name, password)
            user.save()
            # create profile for user
            profile = Profile(user=user)
            profile.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse('auctions:index'))
    else:
        return render(request, "auctions/register.html")


@login_required(login_url='auctions:login')
def listing(request, listing_id):
    """
    get the listing, and the bids for that listing. Determine whether it is in the
    user's watchlist and display this info
    """
    is_watched = False
    is_current_bidder = False
    listing = Listing.objects.get(pk=listing_id)
    is_owner = request.user == listing.owner
    bids = Bid.objects.all().filter(listing=listing)
    profile = Profile.objects.get(pk=request.user)
    watchlist = profile.watchlist.all()
    categories = listing.category.all()
    comments = Comment.objects.filter(listing=listing).order_by('-made_on')
    if len(bids) == 0:
        current_bid = None
    else:
        current_bid = bids.order_by('-bid_date')[0]
        if current_bid.bidder == request.user:
            is_current_bidder = True
    for watched_listing in watchlist:
        if watched_listing.listing_id == listing_id:
            is_watched = True
            break
        else:
            is_watched = False

    return render(request, 'auctions/listing.html', {
        'listing': listing,
        'bid_count': len(bids),
        'is_current_bidder': is_current_bidder,
        'current_bid': current_bid,
        'is_watched': is_watched,
        'is_owner': is_owner,
        'categories': categories,
        'comments': comments,
        'form': AddCommentForm(initial={
            'poster': request.user,
            'id': random_string(70),
            'listing': listing
        })
    })


@login_required(login_url='auctions:login')
def watchlist(request):
    """

    """
    listings = []
    profile = Profile.objects.get(pk=request.user)
    watchlist = profile.watchlist.all()
    for watched_listing in watchlist:
        listing = Listing.objects.get(pk=watched_listing.listing_id)
        if listing.is_active:
            listings.append(listing)

    return render(request, 'auctions/watchlist.html', {
        'listings': listings
    })


def category(request, category_id):
    cat = Category.objects.get(pk=category_id)
    listings = cat.listing_set.all().exclude(owner=request.user)
    try:
        return render(request, 'auctions/category.html', {
            'listings': listings
        })
    except Exception as info:
        raise info


@login_required(login_url='auctions:login')
def create_listing(request):
    if request.method != "POST":
        return render(request, 'auctions/add.html', {
            'form': AddListingForm()
        })
    form = AddListingForm(request.POST)
    if form.is_valid():
        try:
            listing = form.save(commit=False)
            listing.owner = request.user
            listing.is_active = True
            listing.id = f'{random_string(30)}'
            listing.save()
            form.save_m2m()
            listing.refresh_from_db()
            return redirect('auctions:listing', listing.id)
        except Exception as info:
            return render(request, 'auctions/info.html', {
                'info': info
            })
    return render(request, 'auctions/info.html', {
        'info': 'Request was unsuccessful. if problem persists contact your system administrator'
    })


@login_required(login_url='auctions:login')
def bid(request, listing_id):
    listing = Listing.objects.get(id=listing_id)
    rel_bid_set = Bid.objects.all().filter(listing=listing)
    minimum_bid = float(listing.starting_bid)
    # set current bid price
    if len(rel_bid_set) > 0:
        minimum_bid = float(rel_bid_set.order_by("-bid_date")[0].price)
    if request.method == "POST" and float(request.POST["price"]) > minimum_bid:
        price = request.POST['price']
        bidder = request.user
        if bidder == listing.owner:
            return render(request, 'auctions/info.html', {
                'info': 'You are the owner of this listing. You can not bid on it'
            })
        id = random_string(70)
        try:
            bid = Bid(id=id, bidder=bidder, listing=listing, price=float(price))
            bid.save()
            return redirect('auctions:listing', listing_id)
        except Exception as info:
            raise info
    return render(request, 'auctions/info.html', {
        'info': 'Error! Check that your bid is higher than the current bid and try again'
    })


@login_required(login_url='auctions:login')
def end_bidding(request):
    if request.method != "POST":
        return render(request, 'auctions/info.html', {
            'info': 'We could not Process your request. contact your administrator to fix this problem.'
        })
    try:
        listing = Listing.objects.filter(pk=request.POST['listing_id'])
        current_bid = Bid.objects.filter(pk=request.POST['bid_id'])
        current_bid.update(is_winning_bid=True)
        listing.update(is_active=False)
        # remove from all watch-lists
        watches = Watch.objects.filter(listing_id=request.POST['listing_id']).delete()
        return redirect('auctions:listing', request.POST['listing_id'])
    except Exception as info:
        raise info


@login_required(login_url='auctions:login')
def watch(request, listing_id):
    """
    add Watch object with listing to profile
    """
    profile = Profile.objects.get(pk=request.user)
    if profile.user == Listing.objects.get(pk=listing_id).owner:
        return render(request, 'auctions/info.html', {
            'info': 'You are the owner of this Listing and can\'t add it to your watchlist'
        })
    # check that the item is not repeated in the watchlist
    watchlist = profile.watchlist.all()
    watch_exists = False
    listing_name = Listing.objects.get(pk=listing_id).name
    for watched_item in watchlist:
        if listing_id == watched_item.listing_id:
            watch_exists = True
            return render(request, 'auctions/info.html', {
                'info': f'The Item You are trying to add to your watchlist is already in your watchlist '
            })
    if not watch_exists:
        try:
            watch = Watch(id=f'{random_string(70)}', listing_id=listing_id, listing_name=listing_name, watcher_name=f'{request.user.username}')
            watch.save()
            profile.watchlist.add(watch)
            return render(request, 'auctions/info.html', {
                'info': f'You have added item to your watchlist'
            })
        except Exception as info:
            raise info


@login_required(login_url='auctions:login')
def unwatch(request, listing_id):
    """
    get profile for user and check to see if
    """
    profile = Profile.objects.get(pk=request.user)
    watch = Watch.objects.filter(watcher_name=request.user.username, listing_id=listing_id)
    try:
        watch.delete()
        return render(request, 'auctions/info.html', {
            'info': 'successfully removed this item from your blacklist'
        })
    except Exception as info:
        raise info


@login_required()
def my_listings(request):
    listings = Listing.objects.filter(owner=request.user)

    return render(request, 'auctions/mylistings.html', {
        'my_listings': listings,

    })


@login_required(login_url='auctions:login')
def comment(request, listing_id):
    if request.method == "POST":
        form = AddCommentForm(request.POST)
        if form.is_valid():
            if len(form.cleaned_data['content']) == 0:
                return render(request, 'auctions/info.html', {
                    'info': "you can not post an empty comment"
                })
            comment = form.save(commit=False)
            comment.id = random_string(70)
            comment.poster = request.user
            comment.listing = Listing.objects.get(pk=listing_id)
            comment.save()
            comment.refresh_from_db()
            return redirect('auctions:listing', listing_id)


@login_required(login_url='auctions:login')
def categories(request):
    cats = Category.objects.all().order_by('-parent_id')
    return render(request, 'auctions/categories.html', {
        'categories': cats
    })


@login_required(login_url='auctions:login')
def won(request):
    winnings = []
    won_bids = Bid.objects.filter(bidder=request.user, is_winning_bid=True)
    for won_bid in won_bids:
        winnings.append(won_bid.listing)
    return render(request, 'auctions/winnings.html', {
        'listings': winnings
    })
