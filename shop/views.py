from django.shortcuts import render, get_object_or_404
from .models import Brand, Product
from basket.forms import BasketAddProductForm


def product_list(request, category_slug=None):
    brand = None
    categories = Brand.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        brand = get_object_or_404(Brand, slug=category_slug)
        products = products.filter(brand=brand)
    return render(request,
                  'shop/product_list.html',
                  {
                      'brand': brand,
                      'categories': categories,
                      'products': products
                  })


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    basket_product_form = BasketAddProductForm()
    return render(request,
                  'shop/product_detail.html',
                  {'product': product,
                   'basket_product_form': basket_product_form})
