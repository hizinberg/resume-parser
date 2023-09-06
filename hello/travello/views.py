from django.shortcuts import render,HttpResponse
from .forms import ResumeForm
from django import forms
from django.core.files.storage import FileSystemStorage
from pyresparser import ResumeParser
from .skills import find

from .models import Resume
import io
from django.http import FileResponse


# Create your views here.
def index(request):
    if request.method == 'POST':
        resum = request.FILES['res']
        fs = FileSystemStorage()
        fs.save(resum.name,resum)
        return HttpResponse(resum)
    return render(request,'index.html')

def uploadresume(request):
    if request.method == "POST":
        form = ResumeForm(request.POST,request.FILES)
        par = form.save()
        par.save()
        par.skill,par.skillset = getfile(par.resume.path)
        par.save()
        return HttpResponse("resume has been uploaded successfully")
    else:
         form = ResumeForm()   
    return render(request,'index.html',{'form':form})

def getfile(fil):
    data = ResumeParser(fil).get_extracted_data()
    return find(data)



def search(request):
    if request.method=='GET':
        print(request.GET['search'])
        sea = Resume.objects.filter(skill = request.GET['search'])
        relre={'resume':sea}
        return render(request,'index.html',relre)

def pdf_view(request):
    if request.method=='POST':
        val = request.POST.get("abc")
        return FileResponse(open(val,'rb'),content_type='application/pdf') 
    else:
        val=""
    return HttpResponse(val)