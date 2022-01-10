from django.urls import path, include
from rest_framework import routers

from projects.views import ProjectsViewSet

router = routers.DefaultRouter()
router.register('projects', ProjectsViewSet)
urlpatterns = [
    path('', include(router.urls))
]
