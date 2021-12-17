from django.urls import path
from . import views

app_name = "rango_app"
urlpatterns = [
    path('', views.index, name='index'),
    path('receipts/', views.receipts, name='receipt')
]