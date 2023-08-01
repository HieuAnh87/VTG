from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.db.models import Sum
from django.db.models.functions import TruncMonth
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View


class HomeView(View):
    def get(self, request):
        # greeting = {}
        # greeting['heading'] = "Home"
        # greeting['pageview'] = "Home"
        return render(request, 'homepage.html')
