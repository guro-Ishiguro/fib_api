from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path("fib", views.FibViewSet.as_view()),
]
