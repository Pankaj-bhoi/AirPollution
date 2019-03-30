from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context,loader
import csv
# # Here i want to store it in variable a,b,c,d than export it to the csv file
# But is it possible ?
def home(request):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
    return render(request,'index.html')

def GetParam(request):
    a = int(request.GET['co2'])
    b = int(request.GET['no2'])
    c = int(request.GET['zn'])
    d = int(request.GET['h2'])

    # This part copied from internet because i want to see some functionality
    global i
    global j
    global k
    global l
    i = int(a)
    j = int(b)
    k = int(c)
    l = int(d)
    response = HttpResponse(content_type='text/csv')  
    response['Content-Disposition'] = 'attachment; filename="file.csv"'  
    writer = csv.writer(response)  
    writer.writerow(i)  
    writer.writerow(j)  
    writer.writerow(k)  
    writer.writerow(l)
    return response
# def getfile(request):  
    


