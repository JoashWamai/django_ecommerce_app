from django.shortcuts import render, redirect
from django.http import JsonResponse
import json
import sweetify
from django.contrib.auth import authenticate, login, logout
from django.template.loader import render_to_string
import random
from .forms import *
from django.contrib.auth.decorators import login_required
from .models import *
from django.core.paginator import Paginator
from django.db.models import Count
from .filters import *
from django.contrib.auth.decorators import login_required
from .decorators import checkoutDecorator


def register(request):
    form = RegistrationForm()
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            sweetify.success(request, title="Account for " + username + " sucessfully created", icon="success")
            return redirect('home')
        else:
            sweetify.error(request, title='Error', text='Something went wrong try again', icon='error')
            return render(request, 'store/loginRegister.html')
    context = {'form': form}
    return render(request, 'store/loginRegister.html', context)


def loginuser(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('administrator')
            else:
                return redirect('home')
        else:
            sweetify.error(request, title='Error', text='UserName or Password is incorrect', icon='error')
            return render(request, 'store/loginRegister.html')

    return render(request, 'store/loginRegister.html')


def logoutUser(request):
    logout(request)
    return redirect('login')


def home(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    sales = products.filter(tag__tagName='Sale')
    new = products.filter(tag__tagName='New')[:12]

    if request.user.is_authenticated:
        customer = request.user.customer
        order,created = Order.objects.get_or_create(customer=customer)
        wish = Wishlist.objects.get(customer=customer)
        cartItems = order.get_cart_items
        wishItems = wish.get_wish_items
    else:
        cartItems = "[]"
        wishItems = "[]"
    # pf = ProductFilter()

    context = {'products': products, 'categories': categories, 'saleproducts': sales,
               'newproducts': new, 'cartItems': cartItems, 'wishItems': wishItems}
    return render(request, 'store/home.html', context)


def productDetail(request, pk):
    product = Product.objects.get(id=pk)
    oldprice = product.oldPrice
    newprice = product.newPrice
    categories = product.category.all()
    reviews = Review.objects.filter(product=product)

    if request.user.is_authenticated:
        customer = request.user.customer
        order = Order.objects.get(customer=customer,complete=False)
        wish = Wishlist.objects.get(customer=customer)
        # order, created = Order.objects.get_or_create(customer=customer, complete=False)
        # wish, created = Wishlist.objects.get_or_create(customer=customer)
        cartItems = order.get_cart_items
        wishItems = wish.get_wish_items
    else:
        cartItems = "[]"
        wishItems = "[]"

    form = ReviewForm()
    if request.method == "POST":
        form = ReviewForm(request.POST)
        customer = request.user.customer
        if form.is_valid():
            form.save()
            rtext = form.cleaned_data.get('reviewText')
            if rtext is None:
                sweetify.error(request, title='Error', text='Please write your review first', icon='error')
            else:
                sweetify.success(request, title="Thanks for your feedback", icon="success")
                Review.objects.create(customer=customer, product=product, reviewText=rtext)
        else:
            sweetify.error(request, title='Error', text='Something went wrong try again', icon='error')
            return render(request, 'store/product.html')

    for category in categories:
        category_products = category.product_set.all()

    if oldprice != 0:
        discount = int((oldprice - newprice) / oldprice * 100)
    else:
        discount = 0

    context = {'product': product, 'discount': discount, 'categories': category_products,
               'categorynames': categories, 'cartItems': cartItems,
               'wishItems': wishItems, 'reviews': reviews, 'form': form}
    return render(request, 'store/product.html', context)


def categoryDetails(request, pk):
    categories = Category.objects.annotate(category_products=Count('product__productQuantity')).order_by(
        "-category_products")[:5]
    category = Category.objects.get(id=pk)
    products = category.product_set.all()

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        wish, created = Wishlist.objects.get_or_create(customer=customer)
        cartItems = order.get_cart_items
        wishItems = wish.get_wish_items
    else:
        cartItems = "[]"
        wishItems = "[]"

    paginator = Paginator(products, 10)
    page_number = request.GET.get('page')
    pageobj = paginator.get_page(page_number)

    brands = Brand.objects.annotate(brand_products=Count("product__productQuantity")).order_by("-brand_products")[:5]

    context = {'products': products, 'categorylist': categories, 'selectedcat': category,
               'brands': brands, 'pages': pageobj, 'cartItems': cartItems,
               'wishItems': wishItems}
    return render(request, 'store/categories.html', context)


@login_required(login_url='login')
def cart(request):
    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items = order.orderitems_set.all()
    cartItems = order.get_cart_items

    if request.user.is_authenticated:
        customer = request.user.customer
        wish = Wishlist.objects.get(customer=customer)
        wishItems = wish.get_wish_items
    else:
        wishItems = "[]"

    context = {'items': items, 'order': order, 'cartItems': cartItems, 'wishItems': wishItems}
    return render(request, 'store/cart.html', context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data['product']
    action = data['action']

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItems.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.orderQuantity = (orderItem.orderQuantity + 1)
        sweetify.success(request, title=orderItem.product.productName + " sucessfully added to cart", icon="success")
    elif action == 'remove':
        orderItem.orderQuantity = (orderItem.orderQuantity - 1)

    orderItem.save()

    if orderItem.orderQuantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)


@login_required(login_url='login')
def wishlist(request):
    customer = request.user.customer
    wish, created = Wishlist.objects.get_or_create(customer=customer)
    items = wish.wishlistitems_set.all()
    wishItems = wish.get_wish_items

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        cartItems = order.get_cart_items
    else:
        cartItems = "[]"

    context = {'items': items, 'wish': wish, 'cartItems': cartItems, 'wishItems': wishItems}
    return render(request, 'store/wishlist.html', context)


def updateWishList(request):
    data = json.loads(request.body)
    productId = data['product']
    action = data['action']

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    wish, created = Wishlist.objects.get_or_create(customer=customer)

    wishItem, created = WishlistItems.objects.get_or_create(wish=wish, product=product)

    if action == 'add':
        wishItem.wishQuantity = (wishItem.wishQuantity + 1)
        sweetify.success(request, title=wishItem.product.productName + " sucessfully added to wishlist", icon="success")
    elif action == 'remove':
        wishItem.wishQuantity = (wishItem.wishQuantity - 1)

    wishItem.save()

    if wishItem.wishQuantity <= 0:
        wishItem.delete()

    return JsonResponse('Wish Item was added', safe=False)


def cartToWish(request):
    data = json.loads(request.body)
    pid = data["productId"]
    amount = data["quantity"]

    customer = request.user.customer

    product = Product.objects.get(id=pid)

    wish, created = Wishlist.objects.get_or_create(customer=customer)
    wishItem, created = WishlistItems.objects.get_or_create(wish=wish, product=product, wishQuantity=amount)
    wishItem.save()

    orderItem = OrderItems.objects.filter(product__id=pid)
    orderItem.delete()
    sweetify.success(request, title=wishItem.product.productName + " sucessfully moved to wishlist", icon="success")
    print(wishItem)

    return JsonResponse('Cart Item was transfered', safe=False)


def wishtoCart(request):
    data = json.loads(request.body)
    pid = data["productId"]
    amount = data["quantity"]

    customer = request.user.customer

    product = Product.objects.get(id=pid)

    order, created = Order.objects.get_or_create(customer=customer)
    orderItem, created = OrderItems.objects.get_or_create(order=order, product=product, orderQuantity=amount)
    orderItem.save()

    wishItem = WishlistItems.objects.filter(product__id=pid)
    wishItem.delete()
    sweetify.success(request, title=orderItem.product.productName + " sucessfully moved to cart", icon="success")
    print(wishItem)

    return JsonResponse('WishItem Item was transfered', safe=False)


def autocomplete(request):
    if 'term' in request.GET:
        qs = Product.objects.filter(productName__icontains=request.GET['term'])
        results = list()
        for result in qs:
            results.append(result.productName)

        return JsonResponse(results, safe=False)


def search(request):
    if request.method == "GET" and request.is_ajax():
        term = request.GET.get("q")
        print(term)
        products = Product.objects.filter(productName__icontains=term)
        productcount = products.count()

        html = render_to_string(template_name='store/searchresults.html',
                                context={'products': products, "productcount": productcount})
        data_dict = {"html_from_view": html}
        return JsonResponse(data=data_dict, safe=False)

    return render(request, 'store/searchresults.html')


@login_required(login_url='login')
@checkoutDecorator
def checkout(request):
    customer = request.user.customer
    order = Order.objects.get(customer=customer)
    items = order.orderitems_set.all()
    if request.method == "POST":
        data = json.loads(request.body)
        fname = data["fname"]
        lname = data["lname"]
        email = data["email"]
        county = data["county"]
        telephone = data["phone"]
        subcounty = data["subcounty"]
        town = data["town"]

        oid = random.randrange(1000, 2000)
        order, created = Order.objects.get_or_create(customer=customer, orderId=oid, complete=True)

        shoppingdet = ShippingDetails(order=order, customer=customer
                                      , FirstName=fname, LastName=lname,
                                      Email=email, Telephone=telephone,
                                      County=county, SubCounty=subcounty,
                                      Town=town)
        shoppingdet.save()
        sweetify.success(request, title='Success', text='Shipping details successfully', icon='success')

        JsonResponse("data added", safe=False)
    if request.user.is_authenticated:
        wish, created = Wishlist.objects.get_or_create(customer=customer)
        cartItems = order.get_cart_items
        wishItems = wish.get_wish_items
    else:
        cartItems = "[]"
        wishItems = "[]"
    context = {'cartItems': cartItems,
               'wishItems': wishItems,
               "order": order,
               'orderItems': items}
    return render(request, 'store/checkout.html', context)
