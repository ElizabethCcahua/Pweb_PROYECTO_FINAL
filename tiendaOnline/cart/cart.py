class Cart:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        cart = self.session.get("cart")
        if not cart:
            cart = self.session["cart"]={}

        self.cart = cart
    
    def add(self, product):
        """Agregar producto al carrito. Mantener precio unitario fijo.
        """
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {
                "id": product.id,
                "name": product.name,
                "price": float(product.price),  # Mantener precio unitario
                "cant": 1,
                "image": product.image.url if product.image else ""
            }
        else:
            # Aumentar cantidad
            self.cart[product_id]["cant"] += 1
        self.save_cart()

    def save_cart(self):
        self.session["cart"]=self.cart
        self.session.modified=True

    def delete(self,product):
        product.id=str(product.id)
        if product.id in self.cart:
            del self.cart[product.id]
            self.save_cart()

    def subtract_product(self, product):
        """
        Restar producto del carrito.
        """
        product_id = str(product.id)
        if product_id in self.cart:
            self.cart[product_id]["cant"] -= 1
            if self.cart[product_id]["cant"] < 1:
                self.delete(product)  # Eliminar si cantidad llega a 0
        self.save_cart()

    def clean_cart(self):
        """
        Vaciar todo el carrito.
        """
        self.session["cart"] = {}
        self.session.modified = True

