"""BooleanModelIR URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views
import simplexQuery
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    #path('search/ComplexQuery',views.complx,name="complx"),
    path('ComplexQUery/<queryy>/' ,include("complexQuery.urls") , name="ComplexQUery" ),
    path('SimpleQuery/<queryy>/' ,include("simplexQuery.urls") , name="SimpleQuery" ),
    path('Proximity_Query/<queryy>/' ,include("ProximityQuery.urls") , name="Proximity_Query" ),
    #path('search/ComplexQUery/', views.ComplexQUery, name='ComplexQUery'),
    path('okey/' ,views.okey, name="okey" ),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
