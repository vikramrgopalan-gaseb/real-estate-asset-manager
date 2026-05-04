from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Building, Floor

# BUILDING VIEWS
class BuildingList(LoginRequiredMixin, ListView):
    model = Building

class BuildingDetail(LoginRequiredMixin, DetailView):
    model = Building

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
