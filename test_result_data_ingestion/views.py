from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from rest_framework import viewsets
from .models import *
from .serializers import *
from django.views.generic import TemplateView
from django.contrib.messages.views import SuccessMessageMixin
import pandas as pd
import io
import datetime


class PerformanceTestResultsViewSet(viewsets.ModelViewSet):
    serializer_class = PerformanceTestResultsSerializer
    queryset = PerformanceTestResults.objects.all()


class CsvUploader(TemplateView):
    template_name = 'csv_uploader.html'
    success_message = "%(name)s was created successfully"

    def post(self, request):

        csv = request.FILES['csv']
        csv_data = pd.read_csv(io.StringIO(csv.read().decode("utf-8")))
        counter = 0
        exceptions = []
        for record in csv_data.to_dict(orient="records"):
            try:
                # convert unix time to datetime obj
                dt_obj = pd.to_datetime(record['timeStamp'], unit='ms')
                row = PerformanceTestResults.objects.create(
                    execution_time=dt_obj,
                    elapsed_time=record.get('elapsed'),
                    label=record.get('label'),
                    response_code=record.get('responseCode'),
                    response_message=record.get('responseMessage'),
                    thread_name=record.get('threadName'),
                    data_type=record.get('dataType'),
                    success=record.get('success'),
                    failure_message=record.get('failureMessage'),
                    bytes=record.get('bytes'),
                    sent_bytes=record.get('sentBytes'),
                    grp_threads=record.get('grpThreads'),
                    all_threads=record.get('allThreads'),
                    test_url=record.get('URL'),
                    latency=record.get('Latency'),
                    idle_time=record.get('IdleTime'),
                    connect_time=record.get('Connect')
                )
                counter = counter + 1
            except Exception as e:
                print("Exception occurred while inserting csv row into db table")
                exceptions.append(e)

        context = {
            'message': {'success': True, 'rows_inserted': counter, 'exceptions': exceptions}
        }

        return render(request, self.template_name, context)

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")