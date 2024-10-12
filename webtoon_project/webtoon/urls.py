from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import WebtoonViewSet

router = DefaultRouter()
router.register(r'webtoons', WebtoonViewSet, basename='webtoon')

urlpatterns = router.urls
