import datetime
import random

from django.core.management.base import BaseCommand

from app_pandas_data.models import Library
from app_pandas_data.views import *
import pandas as pd

df_student = pd.read_csv(r'/home/mahiti/Downloads/student_library_log - Sheet1.csv')
df_student = df_student.rename(columns={'ID':'Student_Id','Book Name' : 'Bookname'})

class Command(BaseCommand):
    def handle(self, *args, **options):
        student_record = []
        for column, row in df_student.iterrows():
            # student_record.(dict(row))
            library_record = Library(**dict(row))
            self.stdout.write(self.style.SUCCESS(type(library_record)))
            # student_record.append(dict(row))
            student_record.append(library_record)
        # self.stdout.write(self.style.SUCCESS(student_record))        
        Library.objects.bulk_create(student_record)
        self.stdout.write(self.style.SUCCESS('data populated sucessfully'))
        