from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .forms import *
from .models import *
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.core import serializers
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
import random, json
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


def shop(request, id):
    shop = get_object_or_404(Shop, id=id)
    query = dict(request.GET.lists())
    categories = get_shop_categories(shop)
    return render(request, 'eshop/shop/view.html', {"shop":  shop, "categories": categories})


def my_shops(request):
    shops = [a for tup in [list(Shop.objects.filter(admin_group__name=x.name)) for x in request.user.smorteruser.groups.all()] for a in tup]
    return render(request, 'eshop/myshops.html', {"shops":  shops})


def is_shop_admin(user, shop):
    return user.is_authenticated and shop.admin_group in user.smorteruser.groups.all()


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
    if request.method.upper() == 'POST':
        form_input = {**request.POST}
        for x in form_input.keys():
            if "methods" not in x:
                form_input[x] = form_input[x][0]
        form_input["owner"] = request.user.smorteruser
        form_input["owner_id"] = form_input["owner"].id
        admins = form_input["admins"]
        form = ShopCreateForm(form_input, request.FILES)
        if form.is_valid():
            admin_group = SmorterGroup()
            admin_group.name = f"{random.random()}"
            admin_group.save()
            [admin_group.permissions.add(x) for x in SmorterPermission.objects.filter(type="SA")]
            admin_group.save()
            shop = form.save()
            print("a", admin_group)
            shop.admin_group = admin_group
            print("a", shop.admin_group)
            shop.save()
            admin_group.name = f"Shop{shop.id}AdminGroup"
            admin_group.save()
            set_shop_admins(shop, admins)
            detail_form = ShopCreateForm(form_input, request.FILES, instance=shop)
            if detail_form.is_valid():
                shop = detail_form.save()
                shop.admin_group = admin_group
            else:
                print(detail_form.errors)



            return redirect('my_shops')
        else:
            print(form.errors)
    else:
        form = ShopCreateForm()
    return render(request, 'eshop/shop/create.html', {'detail_form': form, "users": User.objects.all(), "method": "POST"})


def delete_shop(request, id):
    shop = Shop.objects.get(id=id)
    if shop.owner == request.user.smorteruser:
        shop.delete()
    return redirect('my_shops')


def leave_shop(request, id):
    shop = Shop.objects.get(id=id)
    request.user.smorteruser.groups.set([x for x in request.user.smorteruser.groups.all() if x != shop.admin_group])
    return redirect('my_shops')


def admin_shop(request, id, tab, item_id=None, *args, **kwargs):
    shop = get_object_or_404(Shop, id=id)
    if is_shop_admin(request.user, shop):
        query = dict(request.GET.lists())
        current = get_shop_current_cat(shop, query)
        bread = [["".join([f'category={sus}&' for sus in current["path"][:i+1]])[:-1], sub] for i, sub in enumerate(current["path"])]
        cur_subs = [x for x in current if x not in ["items", "path"]]
        subs = [["".join([f'category={sus}&' for sus in (current["path"] if "path" in current else []) +[sub]])[:-1], sub] for sub in cur_subs]
        if request.method == 'POST':
            form_input = {**request.POST}

            for x in form_input.keys():
                if "methods" not in x:
                    form_input[x] = form_input[x][0]
            form_input["owner"] = shop.owner
            form_input["owner_id"] = form_input["owner"].id
            form_input["admin_group"] = SmorterGroup.objects.get(name=f"Shop{shop.id}AdminGroup")
            admins = form_input["admins"]
            detail_form = ShopCreateForm(form_input, request.FILES, instance=shop)
            if detail_form.is_valid():
                set_shop_admins(shop, admins)
                detail_form.save()

            else:
                print(detail_form.errors)
        else:
            detail_form = ShopCreateForm(instance=shop)
        return render(request, 'eshop/shop/admin/admin_base.html',
                      {'detail_form': detail_form, "users": User.objects.all(),
                       "method": "PUT", "shop": shop,
                       "tab": tab, "current": current, "query_path": (bread[-1][0] if bread else ""),
                       "bread": bread, "subs": subs,
                       })
    else:
        return redirect("catalog")


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


def get_shop_categories(shop):
    categories = {"items": [], "path": []}
    items = [[x["fields"], x["pk"]] for x in json.loads(serializers.serialize("json", shop.item_set.all()))]
    for item, pk in items:
        cats = item["path"].split("/")
        item["id"] = pk
        add_item(categories, cats, item)
    return categories


def get_shop_current_cat(shop, query):
    cats = get_shop_categories(shop)
    return get_deep_dict(cats, query["category"] if "category" in query else [])


def view_item(request, id):
    item = get_object_or_404(Item, id=id)
    if request.method == 'POST':
        form_input = {**request.POST}
        print(form_input)
        oitem = OrderedItem.objects.create(item=item, specs=form_input["specs"][0], count=form_input["qty"][0])
        request.user.smorteruser.cart.items.add(oitem)
        return HttpResponseRedirect(f"/item/{item.id}/")

    return render(request, "eshop/item/view.html", {"item": item})


def create_item(request, id, *args, **kwargs):
    shop = get_object_or_404(Shop, id=id)
    query = dict(request.GET.lists())
    current = get_shop_current_cat(shop, query)
    if request.method == 'POST':
        form_input = {**request.POST}
        for x in form_input.keys():
            form_input[x] = form_input[x][0]

        form_input["shop"] = shop
        images = request.FILES.getlist('images')
        form = ItemCreateForm(form_input)

        if form.is_valid():
            print(form["specs"])
            item = form.save()

            for img in images:
                ItemImage.objects.create(
                    item=item,
                    image=img,
                    alt=img.name.split(".")[0]
                )
            query = "".join([f'category={sus}&' for sus in item.path.split("/")])[:-1]
            return redirect(f'/shop/{item.shop.id}/admin/items/?{query}')
        else:
            print(form.errors)
    else:
        form = ItemCreateForm()
    return render(request, 'eshop/item/create.html', {
        'item_form': form, "method": "POST",
        "shop": shop, "query_path": "".join([f'category={sus}&' for sus in current["path"]])[:-1],
        "path": "/".join(current["path"])})


def edit_item(request, id, item_id, *args, **kwargs):
    shop = get_object_or_404(Shop, id=id)
    item = get_object_or_404(Item, id=item_id)
    specs = json.loads(item.specs)
    query = dict(request.GET.lists())
    current = get_shop_current_cat(shop, query)
    if request.method == 'POST':
        form_input = {**request.POST}
        for x in form_input.keys():
            form_input[x] = form_input[x][0]

        form_input["shop"] = shop
        images = request.FILES.getlist('images')
        form = ItemCreateForm(form_input, instance=item)

        if form.is_valid():
            item = form.save()

            for img in images:
                ItemImage.objects.create(
                    item=item,
                    image=img,
                    alt=img.name.split(".")[0]
                )
            query = "".join([f'category={sus}&' for sus in item.path.split("/")])[:-1]
            return redirect(f'/shop/{item.shop.id}/admin/items/?{query}')
        else:
            print(form.errors)
    else:
        form = ItemCreateForm(instance=item)
    return render(request, 'eshop/item/create.html', {
        'item_form': form, "method": "PUT",
        "shop": shop, "item": item, "query_path": "".join([f'category={sus}&' for sus in current["path"]])[:-1],
        "path": "/".join(current["path"]), "specs": specs})


def delete_items(request, id):
    shop = get_object_or_404(Shop, id=id)
    query = dict(request.GET.lists())
    ids = query["id"] if "id" in query else []
    subs = query["category"] if "category" in query else []

    if request.user.smorteruser in shop.admin_group.smorteruser_set.all():
        for x in ids:
            Item.objects.get(id=int(x)).delete()

    return redirect(f'/shop/{shop.id}/admin/items/?{"".join([f"category={sus}&" for sus in subs])[:-1]}')


def bs(*args):
    print(*args)

@csrf_exempt
def catalog(request):
    for x in range(20):
        obj = Item.objects.get(pk=34)
        obj.pk = None
        obj.save()
    filters = {x: y[0] for x, y in {**request.POST}.items()}
    for x, y in [["search", None], ["minPrice", None], ["maxPrice", None], ["itemsPerPage", 20], ["page", 1]]:
        if x not in filters:
            filters[x] = y

    items = [x for x in Item.objects.all()]
    if filters["search"] not in [None, ""]:
        items = [x for x in items if filters["search"] in x.title]
    if filters["minPrice"]:
        items = [x for x in items if float(filters["minPrice"]) < float(x.price)]
    if filters["maxPrice"]:
        items = [x for x in items if float(filters["maxPrice"]) > float(x.price)]

    page_items = [[]]
    i = 0
    while len(items) > 0:
        if i < int(filters["itemsPerPage"]):
            page_items[-1].append(items[0])
            items.pop(0)
            i += 1
        else:
            i = 0
            page_items.append([])

    filters["page"] = int(filters["page"])
    if int(filters["page"]) > len(page_items):
        filters["page"] = len(page_items)

    return render(request, 'catalog.html', {"items":  page_items[filters["page"]-1], "filters": filters, "page_count": len(page_items)})


def remove_cart_item(request):
    body = json.loads(request.body)
    try:
        if "item_id" in body:
            item = get_object_or_404(OrderedItem, id=body["item_id"])
            item.delete()
            return HttpResponse("yes", status=200)
        else:
            return HttpResponse("no", status=500)
    except Exception as e:
        return HttpResponse("no", status=500)