from django.urls import path
from .views import home, products, product_detail, contact
from . import views
from .views import cart_view
from .views import remove_from_cart



urlpatterns = [
    path("", views.home, name="home"),
    path("products/", views.products, name="products"),
    path("products/<slug:slug>/", views.product_detail, name="product_detail"),
    path("contact/", views.contact, name="contact"),
    path("add-to-cart/<slug:slug>/", views.add_to_cart, name="add_to_cart"),
    path("cart/", cart_view, name="cart"),
    path("cart/remove/<int:item_id>/", remove_from_cart, name="remove_from_cart"),

]
