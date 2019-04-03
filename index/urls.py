from django.conf.urls import url
from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('index', index),
    path('login', login),
    path('insert_one', insert_one),
    path('01-ajax', ajax1),
    path('01-get', ajax_get),
    path('01-json', json1),
    path('02-json', json2),
    path('check-uphone', check_uphone),
    path('regist', regist),
    path('logout', logout),
    path('js_good', js_good),
    path('add_cart', add_cart),
    path('cart', cart),
    path('get_goods', get_goods),
    path('del_cart', del_cart)
]