from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET
from .models import Brand, Product
from basket.forms import BasketAddProductForm, BasketAddProductMainForm
from django.conf import settings

@require_GET
def product_list(request, category_slug=None):
    brand = None
    categories = Brand.objects.all()
    products = Product.objects.filter(available=True).order_by('id')
    if category_slug:
        brand = get_object_or_404(Brand, slug=category_slug)
        products = products.filter(brand=brand)
    basket_product_form = BasketAddProductMainForm()
    page = request.GET.get('page', 1)
    p = Paginator(products, settings.ITEMS_PER_PAGE)
    return render(request,
                  'shop/product_list.html',
                  {
                      'brand': brand,
                      'categories': categories,
                      'page': p.page(page),
                      'basket_product_form': basket_product_form
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
