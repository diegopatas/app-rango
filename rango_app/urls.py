#TODO explain the import area

# Here I associate URLs to Views
# So I need to import django.urls to use func path and views to create the relationship

from django.urls import path
from . import views

#TODO finish line 13 by create a view for index page - view.index

app_name = "rango_app"
urlpatterns = [
    path('', views.index, name='index')
]