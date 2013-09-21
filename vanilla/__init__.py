__version__ = '0.2.1'
__all__ = (
    'View', 'GenericView', 'GenericModelView',
    'RedirectView', 'TemplateView', 'FormView',
    'ListView', 'DetailView', 'CreateView', 'UpdateView', 'DeleteView'
)

from django.views.generic import View
from vanilla.views import (
    GenericView, RedirectView, TemplateView, FormView
)
from vanilla.model_views import (
    GenericModelView, ListView, DetailView, CreateView, UpdateView, DeleteView
)