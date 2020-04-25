from django.db import models
from django_pandas.managers import DataFrameManager

# Create your models here
class Library(models.Model):
    Name = models.CharField(max_length=30 , default = 'Vasanth')
    Student_Id = models.CharField(max_length=50  , default = 'Y13EC3265')
    Batch = models.CharField(max_length=50  , default = '2016-20')
    Bookname = models.CharField(max_length=50  , default = 'Fundamentals of Electric Circuits (Edition 5)')
    Author = models.CharField(max_length=50  , default = 'Charles K. Alexander, Matthew N. O. Sadiku')
    ReserveDate = models.CharField(max_length=50  , default = '20/03/2020')
    RenewDate = models.CharField(max_length=50  , default = 'NaN')
    objects = DataFrameManager()