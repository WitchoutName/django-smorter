from django.shortcuts import render
from .forms import *
from .models import *
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.core import serializers
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
import random
import operator


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


def admin_shop(request, id, tab, item_id=None, *args, **kwargs):
    shop = get_object_or_404(Shop, id=id)
    items = [x["fields"] for x in json.loads(serializers.serialize("json", Item.objects.all()))] if tab == "items" else []
    query = dict(request.GET.lists())
    categories = {}
    for item in items:
        cats = item["path"].split("/")
        add_item(categories, cats, item)
    current = get_deep_dict(categories, query["category"] if "category" in query else [])
    bread = [["".join([f'category={sus}&' for sus in current["path"][:i+1]])[:-1], sub] for i, sub in enumerate(current["path"])] if "path" in current else []
    cur_subs = [x for x in current if x not in ["items", "path"]]
    subs = [["".join([f'category={sus}&' for sus in (current["path"] if "path" in current else []) +[sub]])[:-1], sub] for sub in cur_subs]
    print(subs)

    print(bread)
    if request.method == 'POST':
        form_input = {**request.POST}

        for x in form_input.keys():
            if "methods" not in x:
                form_input[x] = form_input[x][0]
        form_input["owner"] = shop.owner
        form_input["owner_id"] = form_input["owner"].id
        form_input["admin_group"] = SmorterGroup.objects.get(name=f"Shop{shop.id}AdminGroup")
        admins = form_input["admins"]
        detail_form = ShopCreateForm(form_input, instance=shop)
        if detail_form.is_valid():
            print(shop)
            set_shop_admins(shop, admins)
            detail_form.save()

        else:
            print(detail_form.errors)
    else:
        detail_form = ShopCreateForm(instance=shop)
    return render(request, 'eshop/shop/admin/admin_base.html',
                  {'detail_form': detail_form, "users": User.objects.all(),
                   "method": "PUT", "shop": shop,
                   "tab": tab, "current": current,
                   "bread": bread, "subs": subs,
                   })


def add_item(dic, buffer, item):
    if len(buffer) > 0:
        if buffer[0] not in dic:
            dic[buffer[0]] = {"items": [], "path": (dic["path"] if "path" in dic else []) + [buffer[0]]}
        add_item(dic[buffer[0]], buffer[1:], item)
    else:
        dic["items"].append(item)


def get_deep_dict(dic, path):
    if len(path) > 0 and path[0] in dic:
        return get_deep_dict(dic[path[0]], path[1:])
    else:
        return dic
