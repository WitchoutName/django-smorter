from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('auth/signup/', views.signup, name="signup"),
    path('myshops/', views.my_shops, name="my_shops"),
    path('shop/create/', views.create_shop, name="create_shop"),
    path('shop/delete/<int:id>/', views.delete_shop, name="delete_shop"),
    path('shop/leave/<int:id>/', views.leave_shop, name="leave_shop"),
    path('shop/admin/<int:id>/<slug:tab>/', views.admin_shop, name="admin_shop"),
    path('shop/admin/<int:id>/<slug:tab>/items/<int:item_id>/', views.admin_shop, name="admin_shop"),
]