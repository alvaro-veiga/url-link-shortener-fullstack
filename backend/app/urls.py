from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'urls', views.ShortenedURLViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('stats/<str:short_code>/', views.get_url_stats, name='url_stats'),
    path('<str:short_code>/', views.redirect_to_original, name='redirect_to_original'),
]
