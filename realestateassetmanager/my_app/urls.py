from django.urls import path
from . import views

urlpatterns = [
    path('', views.BuildingList.as_view(), name='building-list'),
    path('signup/', views.signup, name='signup'),
    path('building/<int:pk>/', views.BuildingDetail.as_view(), name='building-detail'),
    path('building/add/', views.BuildingCreate.as_view(), name='building-create'),
    path('building/<int:pk>/update/', views.BuildingUpdate.as_view(), name='building-update'),
    path('building/<int:pk>/delete/', views.BuildingDelete.as_view(), name='building-delete'),
    path('building/<int:building_pk>/floor/add/', views.FloorCreate.as_view(), name='floor-create'),
    path('floor/<int:pk>/edit/', views.FloorUpdate.as_view(), name='floor-update'),
    path('floor/<int:pk>/delete/', views.FloorDelete.as_view(), name='floor-delete'),
]
