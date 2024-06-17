from django.urls import path
from . import views
from .views import FilteredCompaniesCountAPIView, get_states, get_cities, filter_options

app_name = 'query_builder'

urlpatterns = [
    path('', views.QueryBuilder, name="query_builder"),
    path('get-states/', get_states, name='get-states'),
    path('get-cities/', get_cities, name='get-cities'),
    path('filter-options/', filter_options, name='filter-options'),
    path('api/filtered-companies/count/', FilteredCompaniesCountAPIView.as_view(), name='filtered-companies-count'),
]