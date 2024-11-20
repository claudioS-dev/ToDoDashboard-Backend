from rest_framework import routers
from django.urls import path
from .api import CardViewSet, health_check

router = routers.DefaultRouter()
router.register('api/cards', CardViewSet, 'cards')

urlpatterns = router.urls + [
    path('api/health_check', health_check, name='health_check')
]