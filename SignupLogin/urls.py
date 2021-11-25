"""SignupLogin URL Configuration

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
from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.template.defaulttags import url
from django.urls import path
from django.contrib.auth import views as auth_views
from gunicorn.app.pasterapp import serve
from django.views.static import serve

from cluster import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', user_views.home, name='home'),
    path('signup/', user_views.signup, name='signup'),
    path('update/', user_views.update, name='update'),
    path('delete/<int:id>', user_views.delete_user, name='delete'),
    path('update/<int:id>', user_views.update_user, name='update'),
    # path('userdata/<int:pk>', user_views.user_details, name='userdata'),
    # path('user_login/', user_views.user_login, name='login'),
    # path('user_logout/', user_views.user_logout, name='logout'),

    path('login/', auth_views.LoginView.as_view(template_name='cluster/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='cluster/logout.html'), name='logout'),

    url(r'^media/(?P<path>.*)$', serve,{'document_root':  settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]
