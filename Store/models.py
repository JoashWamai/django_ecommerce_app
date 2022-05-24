from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    categoryName = models.CharField(max_length=50, verbose_name='CategoryName', null=True, blank=True)
    categoryImage = models.ImageField(upload_to='Categories', verbose_name='CategoryImage', null=True, blank=True)
    categoryDescription = models.CharField(max_length=50, verbose_name='CategoryDescription', null=True, blank=True)

    def __str__(self):
        return self.categoryName


class Brand(models.Model):
    brandName = models.CharField(max_length=50, verbose_name='BrandName', null=True, blank=True, default='Generic')

    def __str__(self):
        return self.brandName


class Tag(models.Model):
    tagName = models.CharField(max_length=50, verbose_name='BrandName', null=True, blank=True)

    def __str__(self):
        return self.tagName


class Size(models.Model):
    SIZE = [
        ('s', 'Small'),
        ('m', 'Medium'),
        ('l', 'Large'),
        ('xl', 'XLarge'),
    ]
    size = models.CharField(max_length=20, choices=SIZE, verbose_name='ProductSize', null=True, blank=True)

    def __str__(self):
        return self.size


class Color(models.Model):
    COLORS = [
        ('Red', 'Red'),
        ('Black', 'Black'),
        ('Green', 'Green'),
        ('Blue', 'Blue'),
        ('Pink', 'Pink'),
        ('Yellow', 'Yellow'),
        ('Purple', 'Purple'),
        ('Brown', 'Brown'),
    ]
    colorName = models.CharField(max_length=20, choices=COLORS, verbose_name='ProductColor', null=True, blank=True)

    def __str__(self):
        return self.colorName


class Product(models.Model):
    productName = models.CharField(max_length=255, null=True, blank=True, verbose_name='ProductName')
    oldPrice = models.FloatField(null=True, blank=True, verbose_name='OldPrice', default=0.0)
    newPrice = models.FloatField(null=True, blank=True, verbose_name='NewPrice')
    color = models.ManyToManyField(Color, null=True, blank=True, verbose_name='ProductColor')
    availability = models.BooleanField(verbose_name='ProductAvailability')
    description = models.TextField(verbose_name='ProductDescription', blank=True, null=True)
    productImage = models.ImageField(verbose_name='ProductImageUrl', upload_to='Products', null=True, blank=True)
    ratings = models.FloatField(verbose_name='Rating', null=True, blank=True)
    category = models.ManyToManyField(Category, blank=True, null=True, verbose_name='category')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, blank=True, null=True, verbose_name='brand')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, blank=True, null=True, verbose_name='tag')
    size = models.ManyToManyField(Size, blank=True, null=True, verbose_name='sizes')
    productQuantity = models.IntegerField(default=1, verbose_name='Product Quantity')

    @property
    def discount(self):
        return int((self.oldPrice - self.newPrice) / self.oldPrice * 100)

    def __str__(self):
        return self.productName


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='User')
    customerName = models.CharField(max_length=225, verbose_name='CustomerName', blank=True, null=True)
    email = models.EmailField(verbose_name='Email', blank=True, null=True)

    def __str__(self):
        return self.customerName


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name='customer', blank=True, null=True)
    dateCreated = models.DateField(auto_now_add=True, verbose_name='Date Ordered')
    orderId = models.IntegerField(blank=True, null=True, verbose_name='OrderId')
    complete = models.BooleanField(default=False, verbose_name="Cart Completed", null=True, blank=False)

    @property
    def get_cart_total(self):
        orderitems = self.orderitems_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitems_set.all()
        total = sum([item.orderQuantity for item in orderitems])
        return total

    def __str__(self):
        return f"OrderNo: {self.id} - Customer: {self.customer.customerName}"


class OrderItems(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='product', blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='order', blank=True, null=True)
    orderQuantity = models.IntegerField(default=0, verbose_name='Order Quantity', null=True, blank=True)
    dateAdded = models.DateTimeField(auto_now_add=True, verbose_name='DateTime Added')

    @property
    def get_total(self):
        total = self.product.newPrice * self.orderQuantity
        return total

    def __str__(self):
        return f"{self.order.customer.customerName} - {self.product.productName}-Order: {self.order.id}"


class Wishlist(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name='customer', blank=True, null=True)
    dateCreated = models.DateField(auto_now_add=True, verbose_name='Date Ordered')

    @property
    def get_wish_total(self):
        wishitems = self.wishlistitems_set.all()
        total = sum([item.get_total for item in wishitems])
        return total

    @property
    def get_wish_items(self):
        wishitems = self.wishlistitems_set.all()
        total = sum([item.wishQuantity for item in wishitems])
        return total

    def __str__(self):
        return str(self.id)


class WishlistItems(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, verbose_name='product', blank=True, null=True)
    wish = models.ForeignKey(Wishlist, on_delete=models.SET_NULL, verbose_name='wish', blank=True, null=True)
    wishQuantity = models.IntegerField(default=0, verbose_name='WishList Quantity', null=True, blank=True)
    dateAdded = models.DateTimeField(auto_now_add=True, verbose_name='DateTime Added')

    @property
    def get_total(self):
        total = self.product.newPrice * self.wishQuantity
        return total

    def __str__(self):
        return self.product.productName


class ShippingDetails(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name="Customer", null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name="Order", null=True)
    FirstName = models.CharField(max_length=200, verbose_name="FirstName", null=True)
    LastName = models.CharField(max_length=200, verbose_name="LastName", null=True)
    Telephone = models.IntegerField(verbose_name="Telephone", null=True)
    Email = models.EmailField(verbose_name="Email", null=True)
    County = models.CharField(max_length=50, verbose_name="County", null=True)
    SubCounty = models.CharField(max_length=50, verbose_name="SubCounty", null=True)
    Town = models.CharField(max_length=50, verbose_name="Town", null=True)
    DateAdded = models.DateField(auto_now_add=True, verbose_name="Date Added")

    def __str__(self):
        return f"{self.customer} - {self.order}"


class Review(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name='Customer', blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Product', blank=True, null=True)
    reviewText = models.CharField(max_length=500, verbose_name='ReviewText', blank=True, null=True)

    def __str__(self):
        return f"{self.customer} - {self.product}"
