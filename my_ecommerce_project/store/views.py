from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, CartItem, Wishlist, Review 
from django.db.models import Avg
from django.contrib.auth.views import LoginView

def login_view(request):
    return render(request, 'store/login.html')

def product_list(request):
    query = request.GET.get('q')
    products = Product.objects.all()
    if query:
        pass 
    return render(request, 'store/index.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'store/product_detail.html', {'product': product})


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
    
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    
    return redirect('product_list')

@login_required
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    wishlist_item, created = Wishlist.objects.get_or_create(user=request.user, product=product)
    
    return redirect('product_list') 

from django.shortcuts import get_object_or_404, redirect
from .models import Product, Review

@login_required
def add_review(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, id=product_id)
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')
        Review.objects.create(product=product, user=request.user, rating=rating, comment=comment)
    return redirect('product_detail', product_id=product_id)

from django.db.models import Avg

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    reviews = product.reviews.all()
    # Average rating calculation
    avg_rating = reviews.aggregate(Avg('rating'))['rating__avg']
    return render(request, 'store/product_detail.html', {
        'product': product,
        'reviews': reviews,
        'avg_rating': avg_rating
    })

def cart_view(request):
    return render(request, 'store/cart.html')

def wishlist_view(request):
    return render(request, 'store/wishlist.html')