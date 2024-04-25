from django.urls import path
from . import views


urlpatterns = [
    path("fbi", views.FbiViewSet.as_view()),
]
