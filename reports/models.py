# backend/reports/models.py
from django.db import models

class Report(models.Model):
    file_number = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    patient_id = models.CharField(max_length=100)
    diagnosis_title = models.CharField(max_length=225)
    diagnosis_details = models.TextField()
    report_date = models.DateField()

    def __str__(self):
        return f'{self.first_name}{self.last_name}'
    
    