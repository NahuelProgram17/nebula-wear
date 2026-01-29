from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category, Cart, CartItem


def home(request):
    nav_categories = Category.objects.filter(is_active=True)

    return render(request, "core/home.html", {
        "nav_categories": nav_categories,
    })


def products(request):
    category_slug = request.GET.get("category")
    products = Product.objects.all()
    if category_slug:
        products = products.filter(category__slug=category_slug)
    nav_categories = Category.objects.filter(is_active=True)

    return render(request, "core/products.html", {
        "products": products,
        "nav_categories": nav_categories,
    })


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    nav_categories = Category.objects.filter(is_active=True)

    return render(request, "core/product_detail.html", {
        "product": product,
        "nav_categories": nav_categories,
    })


def contact(request):
    nav_categories = Category.objects.filter(is_active=True)

    return render(request, "core/contact.html", {
        "nav_categories": nav_categories,
    })


def add_to_cart(request, slug):
    product = get_object_or_404(Product, slug=slug)

    cart, created = Cart.objects.get_or_create(id=1)

    cart_item, item_created = CartItem.objects.get_or_create(
        cart=cart,
        product=product
    )

    if not item_created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect("product_detail", slug=slug)

def remove_from_cart(request, item_id):
    cart = Cart.objects.get(id=1)
    item = get_object_or_404(CartItem, id=item_id, cart=cart)
    item.delete()
    return redirect("cart")



def cart_view(request):
    cart, created = Cart.objects.get_or_create(id=1)
    items = cart.items.select_related("product")

    total = sum(item.product.price * item.quantity for item in items)

    return render(request, "core/cart.html", {
        "cart": cart,
        "items": items,
        "total": total,
        "nav_categories": Category.objects.filter(is_active=True),
    })




