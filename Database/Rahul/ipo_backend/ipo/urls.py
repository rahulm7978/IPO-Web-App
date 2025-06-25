from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CompanyViewSet, IPOViewSet, DocumentViewSet, UserViewSet, ApplicationViewSet, home

router = DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'ipos', IPOViewSet)
router.register(r'documents', DocumentViewSet)
router.register(r'users', UserViewSet)
router.register(r'applications', ApplicationViewSet)

urlpatterns = [
    path('', home, name='home'),              # ✅ root URL
    path('api/v1/', include(router.urls)),       # APIs under /api/
]
