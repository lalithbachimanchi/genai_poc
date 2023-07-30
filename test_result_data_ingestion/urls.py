from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # url('^csv-uploader/$', CsvUploader.as_view(), name='csv-uploader'),
]