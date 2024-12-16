from django.shortcuts import render
from .cart import Cart
from store.models import Product
from django.shortcuts import redirect

def view_cart(request):
    cart = Cart(request)
    
    return render(request, 'cart/cart.html', {"cart" : cart})

def add_product(request, product_id):

    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    cart.add(product=product)

    return redirect("store")


def delete_product(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    cart.delete(product=product)

    return redirect("store")


def subtract_product(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    cart.subtract_product(product=product)

    return redirect("store")


def clear_cart(request, product_id):
    cart = Cart(request)
    cart.limpiar_cart()

    return redirect("store")