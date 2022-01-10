# Create your views here.
from rest_framework import viewsets

from projects.models import Projects
from projects.serializers import ProjectSerializer


class ProjectsViewSet(viewsets.ModelViewSet):
    queryset = Projects.objects.all()
    serializer_class = ProjectSerializer
