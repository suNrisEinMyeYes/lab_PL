from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from datetime import datetime
from django.core.files.storage import FileSystemStorage
#from somewhere import handle_uploaded_file
import os
import shutil
@api_view(('GET',))
#@renderer_classes((TemplateHTMLRenderer, JSONRenderer))

def index(request):
    #root_dir='/home/mertakov/Desktop'
    root_dir=os.path.dirname(os.path.realpath(__file__))
    full_path =root_dir + request.path
   # split_path = full_path.split('/')
    #if (len(split_path[-1]) < 1):
     #   file = split_path[-2]
      #  folders = split_path[2:len(split_path)-2]
    #else:
     #   file = split_path[-1]
      #  folders = split_path[2:len(split_path)-1]
    os.chdir(full_path)
    #print(full_path)
    return(Response(os.listdir(path='.')))


def cut(url):
    length=len(url)
    return(url[0:length-7])
    


@api_view(('GET',))
def create(request):
    dirname=request.GET.get("q")
    root_dir=os.path.dirname(os.path.realpath(__file__))
    full_path =root_dir + request.path
    os.mkdir(cut(full_path)+dirname)
    return(Response(os.listdir(path='.')))

@api_view(('GET',))
def delete(request):
    dirname=request.GET.get("q")
    root_dir=os.path.dirname(os.path.realpath(__file__))
    full_path =root_dir + request.path
    shutil.rmtree(cut(full_path)+dirname)
    return(Response(os.listdir(path='.')))

@api_view(('GET',))
def downlo(request):
    root_dir=os.path.dirname(os.path.realpath(__file__))
    full_path =root_dir + request.path
    filename = request.GET.get("q")
    path_to_file=cut(full_path)+filename
    file = open(path_to_file,"r")
    response = HttpResponse(file, content_type='application/msword')
    response['Content-Disposition']='attachment; filename='+filename
    return response
    
def upload(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
    return render(request, 'index.html')

