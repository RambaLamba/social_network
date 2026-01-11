"""
URL configuration for web_test project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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

from test_app.views import home, register, logout_view, profile_view, edit_profile, upload_avatar, feed_view, new_publication
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('accounts/login/', auth_views.LoginView.as_view(
            template_name='registration/login.html'
        ), name='login'),
    path('accounts/register/', register, name='register'),
    path('accounts/logout/', logout_view, name='logout'),
    path('profile/', profile_view, name='profile'),
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('upload_avatar/', upload_avatar, name='upload_avatar'),
    path('feed/', feed_view, name='feed'),
    path('new_publication/', new_publication, name='new_publication'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
