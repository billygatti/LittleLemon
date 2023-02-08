#define URL route for index() view
from django.urls import path
from .views import index
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('home', views.index, name='index'),
    path('menu-item', views.MenuItemsView.as_view()),
    path('menu-item/<int:pk>', views.SingleMenuItemView.as_view()),
     path('api-token-auth/', obtain_auth_token),
]
    
