from django.shortcuts import render
import os, glob, io, base64, urllib
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
import matplotlib.pyplot as plt
import pandas as pd
# from fusioncharts import FusionCharts
# Create your views here.
class StudentView(APIView):
    # def file(self, request):
    #     # import ipdb; ipdb.set_trace()
    #     file_path = os.path.abspath('train.csv')
    #     # file_list = os.listdir(file_path + '/csv')
    #     list_of_files = glob.glob('/'.join( file_path.split('/')[0:-1])+str('/media')+str('/*')) # * means all if need specific format then *.csv
    #     latest_file_url = list_of_files

    #     # images =  self.plot_data(latest_file_url)
    #     # # import ipdb; ipdb.set_trace()
    #     # return render(request , 'plot.html' , {'images' : images })
    #     # # /home/mahiti/django/project_pandas/media/train.csv

    def get(self, request):
        # df = pd.read_csv(r'/home/mahiti/Downloads/student_library_log - Sheet1.csv')
        library = Library.objects.all()
        # serializer  = LibrarySerializer(library, many = True)
        df = library.to_dataframe()
        df.plot()
        plotted_fig = plt.gcf()
        buf = io.BytesIO()
        plotted_fig.savefig(buf, format = 'png')
        buf.seek(0)
        img = buf.getvalue()
        # buf.seek(0)
        string = base64.b64encode(img)
        img = urllib.parse.quote(string)
        return render(request , 'index.html' , {'plot' : img })
        # return Response(serializer.data)
