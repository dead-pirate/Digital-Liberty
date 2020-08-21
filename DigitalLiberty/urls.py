"""DigitalLiberty URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,include
from pages.views import about_view,contact_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('about/', about_view,name = 'about'),
    path('contact/', contact_view,name = 'contact'),
    path('posts/', include('blog.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('users/', include('users.urls')),
    # path('create/', create_post,name = 'create_post'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
