from .views import ApiCategoryViews, ApiRecipsViews
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from rest_framework.schemas import get_schema_view


router = DefaultRouter()
router.register('category', ApiCategoryViews)
router.register('recips', ApiRecipsViews)

urlpatterns = [
    path('api/', include(router.urls)),
    path(
        "openapi",
        get_schema_view(title="Recips", description="API for project recips"),
        name="openapi-schema",
    ),

]
