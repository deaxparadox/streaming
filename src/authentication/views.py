from django.shortcuts import render
from django.views.generic import CreateView, TemplateView

from .forms import UserCreateForm

# Login view
class UserCreateView(CreateView):
    template_name = "authentication/register.html"
    form_class = UserCreateForm
    
    
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)