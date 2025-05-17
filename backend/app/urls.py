from django.urls import path
from . import views

urlpatterns = [
    path('shorten/', views.shorten_url, name='shorten_url'),
    path('stats/<str:short_code>/', views.get_url_stats, name='url_stats'),
    path('<str:short_code>/', views.redirect_to_original, name='redirect_to_original'),
]
