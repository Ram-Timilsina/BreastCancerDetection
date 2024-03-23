from django.contrib import admin
admin.site.site_header = "BDR Detection System"
from .models import BreastCancerData,Doctor,Patient,PatientDoctor,BreastScanTestResult,PatientBreastScan
admin.site.register([BreastCancerData,Doctor,Patient,PatientDoctor,BreastScanTestResult,PatientBreastScan])