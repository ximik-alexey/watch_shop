from django.core.paginator import Paginator
from django.forms import IntegerField
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET

from .filter import FilterQuery
from .models import Brand, Product
from basket.forms import BasketAddProductForm, BasketAddProductMainForm
from django.conf import settings


def filter_content(request, products):
    filter = FilterQuery(request)
    if filter.filter_qr.get('filter_number')['filter'] == 1:
        prod = products.order_by('-price')
    elif filter.filter_qr.get('filter_number')['filter'] == 2:
        prod = products.order_by('price')
    elif filter.filter_qr.get('filter_number')['filter'] == 3:
        prod = products.order_by('dimension')
    elif filter.filter_qr.get('filter_number')['filter'] == 4:
        prod = products.order_by('-dimension')
    elif filter.filter_qr.get('filter_number')['filter'] == 5:
        prod = products.order_by('water_resistance_class')
    elif filter.filter_qr.get('filter_number')['filter'] == 6:
        prod = products.order_by('-water_resistance_class')
    elif filter.filter_qr.get('filter_number')['filter'] == 0:
        prod = products.order_by('id')
    return prod


@require_GET
def product_list(request, category_slug=None):
    filter = FilterQuery(request)
    brand = None
    categories = Brand.objects.all().order_by('name')
    products = Product.objects.filter(available=True)
    # print(products)
    if category_slug:
        brand = get_object_or_404(Brand, slug=category_slug)
        products = products.filter(brand=brand)
    if request.GET.get('price') == '1':
        filter.change(1)
    elif request.GET.get('price') == '2':
        filter.change(2)
    elif request.GET.get('dimension') == '1':
        filter.change(3)
    elif request.GET.get('dimension') == '2':
        filter.change(4)
    elif request.GET.get('water') == '1':
        filter.change(5)
    elif request.GET.get('water') == '2':
        filter.change(6)
    elif not request.GET:
        filter.change(0)
    page = request.GET.get('page', 1)
    # print(request.GET)
    products = filter_content(request, products)
    # print(products)
    basket_product_form = BasketAddProductMainForm()
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
