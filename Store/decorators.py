from .models import Order, Wishlist
from django.shortcuts import redirect


def checkoutDecorator(func):
    def wrapperfunc(request, *args, **kwargs):
        customer = request.user.customer
        order = Order.objects.get(customer=customer)
        items = order.get_cart_items
        if items == 0:
            return redirect('home')
        else:
            return func(request, *args, **kwargs)

    return wrapperfunc



