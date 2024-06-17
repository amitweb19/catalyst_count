from django.urls import path
from . import views

app_name = 'upload_data'

urlpatterns = [
    path('', views.UploadData, name='upload_data'),
    path('upload/', views.csv_upload_view, name='csv_upload'),
    path('progress-import/', views.progress_import_view, name='progress_import'),
]