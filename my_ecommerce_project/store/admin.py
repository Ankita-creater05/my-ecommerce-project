from django.contrib import admin
from .models import Category, Product  
from .models import CartItem,Wishlist

admin.site.register(CartItem)
admin.site.register(Wishlist)
admin.site.register(Category)
admin.site.register(Product)


