def total_cart_amount(request):
    total = 0
    cart = request.session.get("cart", {})  # Obtén el carrito de la sesión o un diccionario vacío
    for key, value in cart.items():
        total += float(value["price"])
    return {"total_cart_amount": total}