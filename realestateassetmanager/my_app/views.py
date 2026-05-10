from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Building, Floor

# AUTHENTICATION
def signup(request):
  error_message = ''
  if request.method == 'POST':
    
    form = UserCreationForm(request.POST)
    if form.is_valid():
     
      user = form.save()
      
      login(request, user)
      return redirect('building-list')
    else:
      error_message = 'Invalid sign up - try again'
  
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

# BUILDING CRUD
class BuildingList(LoginRequiredMixin, ListView):
    model = Building
    def get_queryset(self):
        return Building.objects.filter(owner=self.request.user)

class BuildingDetail(LoginRequiredMixin, DetailView):
    model = Building

class BuildingCreate(LoginRequiredMixin, CreateView):
    model = Building
    fields = ['name', 'address']
    success_url = reverse_lazy('building-list')
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class BuildingUpdate(LoginRequiredMixin, UpdateView):
    model = Building
    fields = ['name', 'address']
    success_url = reverse_lazy('building-list')

class BuildingDelete(LoginRequiredMixin, DeleteView):
    model = Building
    success_url = reverse_lazy('building-list')

# FLOOR CRUD
class FloorCreate(LoginRequiredMixin, CreateView):
    model = Floor
    fields = ['floor_number', 'floor_type', 'annual_income']
    def form_valid(self, form):
        form.instance.building = Building.objects.get(pk=self.kwargs['building_pk'])
        return super().form_valid(form)
    def get_success_url(self):
        return reverse_lazy('building-detail', kwargs={'pk': self.kwargs['building_pk']})

class FloorUpdate(LoginRequiredMixin, UpdateView):
    model = Floor
    fields = ['floor_type', 'annual_income']
    def get_success_url(self):
        return reverse_lazy('building-detail', kwargs={'pk': self.object.building.id})

class FloorDelete(LoginRequiredMixin, DeleteView):
    model = Floor
    def get_success_url(self):
        return reverse_lazy('building-detail', kwargs={'pk': self.object.building.id})
