from django.urls import path, include

from rest_framework import routers

from .views import(
    StudentModelViewSet,
    PathModelViewSet
)


router = routers.DefaultRouter()
router.register("students", StudentModelViewSet)  # students/   students/id
router.register("paths", PathModelViewSet)

urlpatterns = [

] + router.urls



# urlpatterns += router.urls