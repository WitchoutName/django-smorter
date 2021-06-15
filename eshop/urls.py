from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('auth/signup/', views.signup, name="signup"),
    path('myshops/', views.my_shops, name="my_shops"),
    path('shop/<int:id>/', views.shop, name="view_shop"),
    path('shop/create/', views.create_shop, name="create_shop"),
    path('shop/<int:id>/delete/', views.delete_shop, name="delete_shop"),
    path('shop/<int:id>/leave/', views.leave_shop, name="leave_shop"),
    path('shop/<int:id>/admin/<slug:tab>/', views.admin_shop, name="admin_shop"),
    path('shop/<int:id>/admin/<slug:tab>/<int:item_id>/', views.admin_shop, name="admin_shop"),
    path('shop/<int:id>/admin/item/create/', views.create_item, name="create_item"),
    path('shop/<int:id>/admin/item/delete/', views.delete_items, name="delete_items"),

]