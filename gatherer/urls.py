from django.urls import path

from . import views

urlpatterns = [
    path('data', views.ListData.as_view()),
    path('data/<int:pk>', views.DetailData.as_view()),
    path('status', views.ListStatus.as_view()),
    path('status/<int:pk>', views.DetailStatus.as_view()),
]
