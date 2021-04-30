import os
from django.http import HttpResponse

import os

file_addr = os.path.abspath (__file__)
file_dir=os.path.dirname(file_addr)

def sample(request):
    return HttpResponse("hello everyone")

def register(request):
    data=""" 
    
    <!DOCTYPE html>
<html>
<head>
    <title>my webpage</title>
</head>
<body style="background-image:url(https://cdn.pixabay.com/photo/2021/01/31/14/31/water-5967218_1280.jpg)">
<h1 style="color: blueviolet;text-align: center;">welcome to my webpage</h1>
<div style="color: rgb(230, 214, 214);" >
<p style="padding: 25px;20px;25p;20px;"> Lorem, ipsum dolor sit amet consectetur adipisicing elit. Molestias temporibus aliquid dicta enim, cupiditate eaque libero dignissimos vero, dolorum unde recusandae atque asperiores nihil? Temporibus corrupti molestiae itaque asperiores ipsam.</p>






</div>




</body>

</html>
    
    
      
    """
def sampleSignup(request):
    file_data=os.path.join(file_dir,"home.html")
    file_d=open(file_data,"r")
    data1=file_d.read()
    return HttpResponce(data1)
