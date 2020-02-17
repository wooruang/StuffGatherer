from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListData.as_view(), "data_list"),
    path('<int:pk>/', views.DetailData.as_view()),
]
