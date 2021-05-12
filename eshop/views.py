from django.shortcuts import render
from .forms import *
from .models import *
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
import random


def home(request):
    return render(request, "eshop/home.html", {})


def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'registration/signup.html', {'form': form})


def my_shops(request):
    shops = [a for tup in [list(Shop.objects.filter(admin_group__name=x.name)) for x in request.user.smorteruser.groups.all()] for a in tup]
    return render(request, 'eshop/myshops.html', {"shops":  shops})


def set_shop_admins(shop, admins):
    if shop:
        for user in SmorterUser.objects.filter(groups__in=[shop.admin_group]):
            user.groups.remove(shop.admin_group)
            user.save()
        for user in admins.split(","):
            u = User.objects.get(username=user)
            u.smorteruser.groups.add(shop.admin_group)
            u.save()

    else:
        print("no shop")


def create_shop(request):
    if request.method == 'POST':
        form_input = {**request.POST}
        for x in form_input.keys():
            if "methods" not in x:
                form_input[x] = form_input[x][0]
        form_input["owner"] = request.user.smorteruser
        form_input["owner_id"] = form_input["owner"].id
        admins = form_input["admins"]
        form = ShopCreateForm(form_input)
        if form.is_valid():
            admin_group = SmorterGroup()
            admin_group.name = f"{random.random()}"
            admin_group.save()
            [admin_group.permissions.add(x) for x in SmorterPermission.objects.filter(type="SA")]
            admin_group.save()
            shop = form.save()
            shop.admin_group = admin_group
            shop.save()
            admin_group.name = f"Shop{shop.id}AdminGroup"
            set_shop_admins(shop, admins)
            shop.admin_group.save()

            return redirect('my_shops')
        else:
            print(form.errors)
    else:
        form = ShopCreateForm()
    return render(request, 'eshop/shop/create.html', {'detail_form': form, "users": User.objects.all(), "method": "POST"})


def delete_shop(request, id):
    shop = Shop.objects.get(id=id)
    print("auth", shop.owner, request.user.smorteruser)
    if shop.owner == request.user.smorteruser:
        shop.delete()
    return redirect('my_shops')


def leave_shop(request, id):
    shop = Shop.objects.get(id=id)
    request.user.smorteruser.groups.set([x for x in request.user.smorteruser.groups.all() if x != shop.admin_group])
    return redirect('my_shops')


def admin_shop(request, id):
    shop = get_object_or_404(Shop, id=id)
    if request.method == 'POST':

        form_input = {**request.POST}

        for x in form_input.keys():
            if "methods" not in x:
                form_input[x] = form_input[x][0]
        form_input["owner"] = shop.owner
        form_input["owner_id"] = form_input["owner"].id
        form_input["admin_group"] = SmorterGroup.objects.get(name=f"Shop{shop.id}AdminGroup")
        admins = form_input["admins"]
        print(form_input)
        print("-"*100)
        detail_form = ShopCreateForm(form_input, instance=shop)

        print(detail_form.is_valid())
        if detail_form.is_valid():
            print(shop)
            set_shop_admins(shop, admins)
            detail_form.save()

        else:
            print(detail_form.errors)
    else:
        detail_form = ShopCreateForm(instance=shop)
    return render(request, 'eshop/shop/admin.html', {'detail_form': detail_form, "users": User.objects.all(), "method": "PUT", "shop": shop})