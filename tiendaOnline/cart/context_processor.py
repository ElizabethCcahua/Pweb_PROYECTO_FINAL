def total_cart_amount(request):
    total = 0
    if "cart" in request.session:
        for key, value in request.session["cart"].items():
            total += float(value["price"]) * value["cant"]  # Calcular subtotal por cantidad
    return {"total_cart_amount": total}
