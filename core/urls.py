# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include  # add this
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from authentication import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),          # Django admin route
    path(
        '',
        include('dashboard.urls')),
    path(
        'history/',
        include('history.urls')),
    path(
        'collection/',
        include('collection.urls')),
    # path(
    #     'login/',
    #     auth_views.LoginView.as_view(template_name='base/login.html'),
    #     name='login'),
    # path(
    #     'logout/',
    #     auth_views.LogoutView.as_view(template_name='base/logout.html'),
    #     name='logout'),
    path('login/', auth_views.login_view, name="login"),
    path('register/', auth_views.register_user, name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('social_login/', include('allauth.urls')),
] +  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
