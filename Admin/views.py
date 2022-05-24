from django.shortcuts import render, redirect
from Store.models import *
from .forms import ProductForm
import sweetify
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url='login')
def home(request):
    ordercount = Order.objects.count()
    customercount = Customer.objects.count()
    productcount = Product.objects.count()

    customers = Customer.objects.all()
    orders = OrderItems.objects.filter(order__complete=True).order_by('-dateAdded')[:7]

    context = {'allorders': ordercount, 'allcustomers': customercount, 'allproducts': productcount,
               'customers': customers, 'orders': orders}

    return render(request, 'admin/admin.html', context)


@login_required(login_url='login')
def products(request):
    productlist = Product.objects.all().order_by('id')

    context = {'products': productlist}
    return render(request, 'admin/products.html', context)


@login_required(login_url='login')
def addproduct(request):
    form = ProductForm()

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            product = form.cleaned_data.get('productName')
            sweetify.success(request, title=product + " sucessfully added", icon="success")
            return redirect('administrator')
    context = {'form': form}
    return render(request, 'admin/addProduct.html', context)


@login_required(login_url='login')
def updateproduct(request, pk):
    product = Product.objects.get(id=pk)
    form = ProductForm(instance=product)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)

        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('productName')
            sweetify.success(request, title=name + " sucessfully updated", icon="success")
            return redirect('administrator')

    context = {'form': form}
    return render(request, 'admin/addProduct.html', context)


@login_required(login_url='login')
def statistics(request):
    labels = []
    data = []

    categories = Category.objects.all()

    for category in categories:
        labels.append(category.categoryName)
        data.append(category.product_set.all().count())

    context = {'labels': labels, 'data': data}

    return render(request, 'admin/statistics.html', context)
