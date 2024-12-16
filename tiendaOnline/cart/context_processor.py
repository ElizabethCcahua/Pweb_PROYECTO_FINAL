def total_cart_amount(request):
    total = 0
    if request.user.is_authenticated:
        for key, value in request.session["cart"].items():
            total=total+float(value["price"])
    else:
        total="Debes hacer login"

    return {"total_cart_amount":total}