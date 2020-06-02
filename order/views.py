from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm, OrderCreateAnonForm
from basket.basket import Basket


def order_create(request):
    user = request.user
    print(user.username)
    basket = Basket(request)
    if request.method == 'POST':
        if user.username != '':
            form = OrderCreateForm(request.POST)
        else:
            form = OrderCreateAnonForm(request.POST)
        if form.is_valid():
            order = form.save()
            if not form.data['phone']:
                order.first_name = user.first_name
                order.phone = str(user)
                order.save()

            for item in basket:

                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])

            basket.clear()

            return render(request, 'order/created.html',
                          {'order': order})
    else:
        if user.username != '':
            form = OrderCreateForm
        else:
            form = OrderCreateAnonForm

    return render(request, 'order/order.html',
                  {'basket': basket, 'form': form})
