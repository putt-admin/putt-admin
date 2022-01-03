# Create your views here.
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView
from django.views.generic.detail import SingleObjectMixin

from dashboards.mixins import JSONResponseMixin
from projects.models import Projects


class ProjectListView(ListView, JSONResponseMixin):
    model = Projects
    paginate_by = 10

    def render_to_response(self, context, **response_kwargs):
        return self.render_to_json_response(context, **response_kwargs)


class ProjectCreatView(CreateView):
    model = Projects
    fields = ['name', 'remark', 'is_active']


class ProjectUpdateView(UpdateView):
    model = Projects
    fields = ['name', 'remark', 'is_active']
    template_name_suffix = '_update_form'


class ProjectSingleObjectView(View, SingleObjectMixin):
    model = Projects

    def render_to_response(self, context, **response_kwargs):
        return self.render_to_json_response(context, **response_kwargs)

    def get(self, request):
        self.object = self.get_object()
        context = self.get_context_data()
        return self.render_to_response(context)

    def post(self, request):
        if request.POST.get('pk'):
            view = ProjectUpdateView.as_view()
            return view(request)
        else:
            view = ProjectCreatView.as_view()
            return view(request)
