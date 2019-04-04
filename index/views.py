import json
import random

from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *


# Create your views here.
def index(request):
    if request.method == 'GET':
        # for k ,v in request.session.items():
        #     print(k)
        if 'uphone' in request.session or 'uphone' in request.COOKIES:
            print(request.session['uphone'])
            name = User.objects.filter(phone=request.session['uphone'])
            if name:
                name=name[0]
            # print(request.COOKIES['sessionid'])
            goods = Good.objects.all()
            # resp.delete_cookie('uphone')
            # resp.delete_cookie('upwd')
            # del request.session['uphone']
            # del request.session['upwd']
        print(locals())
        # print(request.user)   # 自带一个request.user 可以在模板中直接用 user 取到 所以不要取名为 user 传到模板中
        resp = render(request, 'index.html', locals())
        return resp


def login(request):
    if request.method == 'GET':
        if 'uphone' in request.session:
            return redirect('/index')
        red = render(request, '00-regist.html')
        ref = request.META.get('HTTP_REFERER', '/index')
        red.set_cookie('ref', ref)
        return red
    else:
        # print(request.session['uphone'])
        uphone = request.POST.get('uphone')
        upwd = request.POST.get('upwd')
        user = User.objects.filter(phone=uphone, pwd=upwd)
        ref = request.COOKIES.get('ref')
        if user:
            request.session['uphone'] = uphone
            request.session['upwd'] = upwd
            response = redirect(ref, locals())
            response.delete_cookie('ref')
            if 'isSave' in request.POST:
                response.set_cookie('uphone', uphone)
            return response
        else:
            return render(request, '00-regist.html')


def insert_one(request):
    user1 = User(name='ppp', phone='654798123', pwd='ppp888')
    user2 = User(name='zww', phone='465123645', pwd='zww777')
    user3 = User(name='hhh', phone='654987324', pwd='hhh000')
    user1.save()
    user2.save()
    user3.save()
    return HttpResponse('ok')


def regist(request):
    if request.method == 'POST':
        phone = request.POST.get('uphone')
        pwd = request.POST.get('upwd')
        name = request.POST.get('name')
        user = User(name=name, phone=phone, pwd=pwd)
        user.save()
        request.session['uphone'] = phone
        return redirect('/login')
    else:
        return render(request, 'regist.html')


def ajax1(request):
    return render(request, '01-ajax.html')


def ajax_get(request):
    return HttpResponse('这就是你发过来的AJAX')


def json1(request):
    dic = {
        'name': 'jhl',
        'age': 19,
        'email': 'jklwefjwklef@qq.com',
    }
    js = json.dumps(dic)
    return HttpResponse(js)


def json2(request):
    users = User.objects.all()
    jsonstr = serializers.serialize('json', users)
    print(jsonstr)
    return HttpResponse(jsonstr)


def check_uphone(request):
    phone = request.POST.get('uphone')
    if phone:
        user = User.objects.filter(phone=phone)
        if user:
            print('手机号已存在')
            return HttpResponse('手机号已存在')
        else:
            return HttpResponse('OK')
    else:
        print('请输入手机号')
        return HttpResponse('请输入手机号')


def logout(request):
    # user = User.objects.get(id=id)
    ref = request.META.get('HTTP_REFERER')
    red = redirect(ref)

    if 'uphone' in request.COOKIES:
        print('del uphone cookie')
        red.delete_cookie('uphone')
    if 'upwd' in request.session:
        del request.session['upwd']
        print('del upwd session')

    if 'uphone' in request.session:
        del request.session['uphone']
        print('del uphone session')

    if 'sessionid' in request.COOKIES:
        print('del sessionid')
        red.delete_cookie('sessionid')

    return red


def js_good(request):
    goods = Good.objects.all()
    goodtypes = GoodType.objects.all()
    jsons = []
    for goodtype in goodtypes:
        dic = {'type': goodtype.to_dict(),
               'good': []}
        for good in goods:
            if good.type == goodtype:
                good_dic = good.to_dict()
                dic['good'].append(good_dic)
        jsons.append(dic)
    jsons = json.dumps(jsons)
    return HttpResponse(jsons)


def cart(request):
    if 'uphone' in request.session:
        uphone = request.session['uphone']
        name = User.objects.filter(phone=uphone)
        if name:
            name=name[0]
    return render(request, 'cart.html', locals())


def add_cart(request):
    print('addcart')
    response = {
        'message': 0
    }
    if 'uphone' in request.session:
        phone = request.session['uphone']
    elif 'uphone' in request.COOKIES:
        phone = request.COOKIES['uphone']
    else:
        return HttpResponse(json.dumps(response))
    print('reqget',request.GET.get('gid'))
    good = Good.objects.get(id=request.GET.get('gid'))
    user = User.objects.get(phone=phone)
    incart = Cart.objects.filter(good=good.id)
    if incart:
        incart[0].num += 1
        incart[0].save()
    else:
        new_cart = Cart(good=good, user=user, num=1)
        new_cart.save()
    response['message'] =1
    print(response)
    return HttpResponse(json.dumps(response))


def get_goods(request):
    user = User.objects.get(phone=request.session['uphone'])
    carts = Cart.objects.filter(user=user)
    my_goods=[]
    for car in carts:
        my_goods.append(car.to_dict())
    print(my_goods)
    return HttpResponse(json.dumps(my_goods))


def del_cart(request):
    user = User.objects.get(phone=request.session["uphone"])
    good = Good.objects.get(id=request.POST['gid'])
    car = Cart.objects.get(good=good, user=user)
    car.delete()
    return HttpResponse('OK')
