from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CompanyViewSet, IPOViewSet, DocumentViewSet,home

router = DefaultRouter()
router.register('companies', CompanyViewSet)
router.register('ipos', IPOViewSet)
router.register('documents', DocumentViewSet)

urlpatterns = [
    path('',home),
    path('', include(router.urls)),
]
