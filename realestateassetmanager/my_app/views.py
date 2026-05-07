from django.views import generic
from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .models import Building, Floor

# BUILDING VIEWS
class BuildingList(LoginRequiredMixin, ListView):
    model = Building

    def get_queryset(self):
        # Only return buildings owned by the current user
        return Building.objects.filter(owner=self.request.user)

class BuildingDetail(LoginRequiredMixin, DetailView):
    model = Building

    def get_queryset(self):
        # Ensures that if a user tries to access a building ID they don't own, 
        # Django will throw a 404 "Not Found" error
        return Building.objects.filter(owner=self.request.user)

class BuildingCreate(LoginRequiredMixin, CreateView):
    model = Building
    fields = ['name', 'address']
    success_url = reverse_lazy('building-list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

# FLOOR VIEWS
class FloorCreate(LoginRequiredMixin, CreateView):
    model = Floor
    fields = ['building', 'floor_number', 'floor_type', 'annual_income']
    success_url = reverse_lazy('building-list')

class FloorUpdate(LoginRequiredMixin, UpdateView):
    model = Floor
    fields = ['floor_type', 'annual_income']
    success_url = reverse_lazy('building-list')

class FloorDelete(LoginRequiredMixin, DeleteView):
    model = Floor
    success_url = reverse_lazy('building-list')

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('building-list')
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        # 1. Save the user to the database
        user = form.save()
        # 2. Log the user in manually
        login(self.request, user)
        # 3. Redirect to the success_url (portfolio)
        return super().form_valid(form)