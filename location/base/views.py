from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .resources import *
from django.contrib import messages
import pandas as pd
import googlemaps

# Create your views here.
def add_points(data):#     data['latitude'] =None
    data['longitude'] = None
    for i in range(0, len(data)):
        geocode_res = gmaps_key.geocode(data.iat[i,0])
        try:
            lat = geocode_res[0]['geometry']['location']['lat']
            lng = geocode_res[0]['geometry']['location']['lng']
            data.iat[i,data.columns.get_loc("latitude")] = lat
            data.iat[i,data.columns.get_loc("longitude")] = lng
        except:
            lat = None
            lng = None
    return data

def upload(request):
    if request.method == "POST":
        dir_resource = DirectionResource()
        filehandle = request.FILES['file']

        if not filehandle.name.endswith('xlsx'):
            messages.info(request,'Please upload in .xlsx format')
            return render(request, 'upload_form.html')

        imported_data = pd.read_excel(filehandle)
        # final_data = add_points(imported_data)
        for ind,data in imported_data.iterrows():
            value = Direction(
                    ind,
                    data[0],
                    data[1],
                    data[2]
            )
            value.save()

    return render(
        request,
        'upload_form.html',
        {
            'title': 'filehandle',
            'header': ('Download your file')
        })

def download(request):
    return render(request,"download_file.html")

def export(request):
    dir_resource = DirectionResource()
    dataset = dir_resource.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="download.xls"'
    return response
