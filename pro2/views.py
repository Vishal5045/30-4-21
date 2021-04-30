from django.http import HttpResponse
import os

file_addr=os.path.abspath(__file__)
file_dir=os.path.dirname(file_addr)

def SampleSignup(request):
    file_data=os.path.join(file_dir,"home.html")
    file_d=open(file_data,'r')
    data1=file_d.read()
    return HttpResponse(data1) 