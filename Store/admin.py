from django.contrib import admin
from .models import *

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(Tag)
admin.site.register(Brand)
admin.site.register(Size)
admin.site.register(Color)
admin.site.register(OrderItems)
admin.site.register(Wishlist)
admin.site.register(WishlistItems)
admin.site.register(Review)
admin.site.register(ShippingDetails)
