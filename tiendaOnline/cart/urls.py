from django.urls import path
from .import views

app_name="cart"

urlpatterns = [
    path("view_cart/", views.view_cart, name="view_cart"),
    path("add/<int:product_id>/", views.add_product, name="add"),
    path("delete/<int:product_id>/", views.delete_product, name="delete"),
    path("subtract/<int:product_id>/", views.subtract_product, name="subtract"),
    path("clear/", views.clear_cart, name="clear"),
    path("make_order/", views.make_order, name="make_order"),
    path("make_order/", views.make_order, name="make_order"),

]