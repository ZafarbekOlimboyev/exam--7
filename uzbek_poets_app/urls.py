from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import PoetsViewSet, PoemsViewSet

router = DefaultRouter()


router.register(r'poets', PoetsViewSet)
router.register(r'poems', PoemsViewSet)

urlpatterns = router.urls
