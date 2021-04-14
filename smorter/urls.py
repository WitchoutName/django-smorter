"""smorter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
# Třída RedirectView, která je součástí balíku django.views.generic umožňuje přesměrování pohledů (stránek)
from django.views.generic import RedirectView
# Z balíku django.conf importujeme nastavení (settings)
from django.conf import settings
# Z balíku django.conf.urls.static importujeme metodu static(),
# pomocí které zajistíme obsluhu statických souborů (jen ve vývojové fázi aplikace)
from django.conf.urls.static import static
# Mapování URL adres webu -propojení URL s jejich obsluhou
urlpatterns = [path('admin/', admin.site.urls),
               path('eshop/', include('eshop.urls')),
               path('', RedirectView.as_view(url='eshop/'))
               ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
