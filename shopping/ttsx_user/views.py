from django.shortcuts import render
from django.http import HttpResponse
import os


# Create your views here.
def index(request):
    # BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # return HttpResponse(BASE_DIR)
    return render(request, 'ttsx_user/index.html')
