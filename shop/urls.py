from django.urls import path
from . import views

# urlpatterns = [
#     path('', views.home, name='home'),
# from django.conf.urls import url
# from . import views
app_name = "shop"
urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('shop/<category_slug>', views.product_list, name='product_list_by_category'),
    path('shop/<id>/<slug>', views.product_detail, name='product_detail'),
]
