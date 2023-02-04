#define URL route for index() view
from django.urls import path
from .views import home
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('menu-item', views.MenuItemsView.as_view()),
    path('menu-item/<int:pk>', views.SingleMenuItemView.as_view()),
]
    
