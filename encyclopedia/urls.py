from django.urls import path

from . import views

app_name = 'wiki'

urlpatterns = [
    path('wiki/<str:title>/edit/', views.edit_entries, name="edit-entries"),
    path('wiki/create/', views.create_entries, name="create-entries"),
    path('wiki/<str:title>/', views.single_entries, name="single-entries"),
    path('wiki/random', views.random_entry, name='random'),
    path("", views.index, name="index"),
]
