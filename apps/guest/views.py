from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from .models import Guest
from .serializers import GuestSerielizer
from django.shortcuts import render
from ..booking.models import Booking
from django.urls import reverse_lazy
from .forms import SignupForm
from django.views.generic import CreateView

class GuestViewSet(ModelViewSet):
    queryset = Guest.objects.all()
    serializer_class = GuestSerielizer

def my_booking(request):
    if request.user.is_authenticated:
        bookings = Booking.objects.filter(guest=request.user)
        context = {
            'bookings': bookings
        }
        return render(request, 'accounts/account.html', context=context)
    else:
        return render(request, 'accounts/account.html')
    
class SignupView(CreateView):
    form_class = SignupForm
    template_name = 'registration/signup.html'
    succes_url = reverse_lazy('login')
    context_object_name = 'signup'


def LoginPage(request):
    return render(request, 'registration/login.html')