from django.shortcuts import render
from .cart import Cart
from store.models import Product
from django.shortcuts import redirect
from django.http import Http404
from django.shortcuts import render

def view_cart(request):
    cart = Cart(request)
    cart_with_subtotals = []

    # Calcular subtotales
    for key, item in cart.cart.items():
        subtotal = float(item["price"]) * int(item["cant"])
        cart_with_subtotals.append({
            "id": item["id"],
            "name": item["name"],
            "image": item["image"],
            "cant": item["cant"],
            "price": item["price"],
            "subtotal": subtotal
        })

    # Pasar al template
    total = sum(item["subtotal"] for item in cart_with_subtotals)
    return render(request, 'cart/cart.html', {
        "cart": cart_with_subtotals,
        "total_cart_amount": total
    })

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


def clear_cart(request):
    cart = Cart(request)
    cart.clean_cart()
    return redirect("cart:view_cart")

def make_order(request):
    # Función vacía para "Hacer Pedido"
    return redirect("cart:view_cart")
