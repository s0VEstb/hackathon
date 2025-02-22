from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PlaceViewSet, UniversityViewSet

router = DefaultRouter()
router.register(r'places', PlaceViewSet)
router.register(r'programs', UniversityViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
