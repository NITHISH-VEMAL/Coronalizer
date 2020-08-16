from django.urls import path
from . import views


urlpatterns = [
    path('model/', views.MyModelListView.as_view(), name='MyModel'),
    path('news/', views.news, name='MyNews'),
    path('about/', views.about, name='about'),
]
