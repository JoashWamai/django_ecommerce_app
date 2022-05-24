from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('cart/', views.cart, name="cart"),
    path('wishlist/', views.wishlist, name="wishlist"),
    path('checkout/', views.checkout, name="checkout"),
    path('product/<int:pk>/', views.productDetail, name="product"),
    path('categories/<int:pk>', views.categoryDetails, name="category-detail"),

    path('login/', views.loginuser, name="login"),
    path('register/', views.register, name="register"),
    path('logout/', views.logoutUser, name="logout"),

    path('updateItem/', views.updateItem, name="updateitem"),
    path('updateWishList/', views.updateWishList, name="updateWishList"),

    path("cartToWishlist/", views.cartToWish, name="carttowish"),
    path("wishlistToCart/", views.wishtoCart, name="wishtocart"),

    path('search/', views.search, name="search"),
    path('autocomplete/', views.autocomplete, name="autocomplete"),
]
