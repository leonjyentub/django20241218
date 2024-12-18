"""
URL configuration for messageboard project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from mymessages import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.message_list, name='message_list'),
    
    # 用戶認證
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='mymessages/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),  # 修改这里
    
    # 留言管理
    path('message/edit/<int:message_id>/', views.edit_message, name='edit_message'),
    path('message/delete/<int:message_id>/', views.delete_message, name='delete_message'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)