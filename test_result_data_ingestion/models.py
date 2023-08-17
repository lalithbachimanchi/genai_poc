from django.db import models

# Create your models here.
from django.db import models


class PerformanceTestResults(models.Model):
    id = models.AutoField(primary_key=True)
    execution_time = models.DateTimeField(null=True)
    elapsed_time = models.IntegerField(null=True)
    label = models.CharField(blank=True,max_length=255)
    response_code = models.CharField(blank=True, max_length=10)
    response_message = models.CharField(blank=True,max_length=255)
    thread_name = models.TextField(null=True)
    data_type = models.CharField(blank=True,max_length=255)
    success = models.BooleanField(default=None, null=True)
    failure_message = models.CharField(blank=True,max_length=255)
    bytes = models.IntegerField(null=True)
    sent_bytes = models.IntegerField(null=True)
    grp_threads = models.IntegerField(null=True)
    all_threads = models.IntegerField(null=True)
    test_url = models.TextField(blank=True)
    latency = models.IntegerField(null=True)
    idle_time = models.IntegerField(null=True)
    connect_time = models.IntegerField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


class APITestResults(models.Model):
    id = models.AutoField(primary_key=True)
    build_number = models.IntegerField(null=True)
    test_name = models.CharField(blank=True,max_length=255)
    test_execution_time_in_secs = models.FloatField(null=True)
    outcome = models.CharField(blank=True,max_length=255)
    error_message = models.TextField(blank=True)
    traceback = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)