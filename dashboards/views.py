# Create your views here.
from django.views.generic import ListView

from dashboards.mixins import JSONResponseMixin
from dashboards.models import Projects


class ProjectView(ListView, JSONResponseMixin):
    model = Projects
    paginate_by = 10

    def render_to_response(self, context, **response_kwargs):
        return self.render_to_json_response(context, **response_kwargs)



