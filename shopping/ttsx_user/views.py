from django.shortcuts import render
from django.http import HttpResponse
from models import *


# Create your views here.
def index(request):
    userlist = userInfo.objects.all()
    context = {'userInfo': userlist}
    # BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # return HttpResponse(BASE_DIR)
    return render(request, 'ttsx_user/index.html', context)
