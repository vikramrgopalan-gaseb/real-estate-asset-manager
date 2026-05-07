from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.BuildingList.as_view(), name='building-list'),
    path('building/<int:pk>/', views.BuildingDetail.as_view(), name='building-detail'),
    path('building/add/', views.BuildingCreate.as_view(), name='building-create'),
    path('floor/add/', views.FloorCreate.as_view(), name='floor-create'),
    path('floor/<int:pk>/update/', views.FloorUpdate.as_view(), name='floor-update'),
    path('floor/<int:pk>/delete/', views.FloorDelete.as_view(), name='floor-delete'),
    path('accounts/', include('django.contrib.auth.urls')),
]
