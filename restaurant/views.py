from django.shortcuts import render
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from .serializers import menuSerializer, bookingSerializer
from .models import Menu, Booking

# Create your views here.
def home(request):
    return render(request, 'home.html', {})

class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = menuSerializer
    
class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = menuSerializer

class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = bookingSerializer