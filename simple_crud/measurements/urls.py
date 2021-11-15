from rest_framework.routers import DefaultRouter
from .api_views import ProjectViewSet, MeasurementViewSet

router = DefaultRouter()
router.register('projects', ProjectViewSet)
router.register('measurements', MeasurementViewSet)

urlpatterns = router.urls
