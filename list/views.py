from multiprocessing import context
from urllib import request
from django.shortcuts import render
from .serializers import HomeSerializer
from .models import Home
from django.views.generic import CreateView
from .forms import HomeForm
from django.urls import reverse_lazy 
from django.conf import settings

class HomeView(CreateView):
    model = Home
    form_class = HomeForm
    template_name = 'home.html'
    success_url = reverse_lazy('home')

    def index(request):
        context = {
            "captcha": HomeForm,
        }
        return render('home.html', context)
