import os 
from django.http import HttpResponse

def getImage(request):
    path = request.GET.get('path', '')
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    d = base_dir
    imagepath = os.path.join(d, "images/" + path)
    print(imagepath)
    image_data = open(imagepath, "rb").read()
    return HttpResponse(image_data, content_type="image/jpg")