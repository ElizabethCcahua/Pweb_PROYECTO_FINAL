from django.shortcuts import render
from store.models import Product

def home(request):
    men = Product.objects.filter(categories_id=1)
    women = Product.objects.filter(categories_id=2)
    kid = Product.objects.filter(categories_id=3)

    context = {
        'men' : men,
        'women' : women,
        'kid' : kid,
    }

    return render(request, 'tiendaApp/index.html', context)