from django.shortcuts import render
from ges.VolumeHandControl import *
from ges.eye import *
from ges.zoom import *
from ges.snake import *
from ges.VirtualMouse import *
from django.shortcuts import HttpResponse

# Create your views here.
def ctrl():
    vctr()


def vmCall():
    vm()

def zoomcall(req):
    return render(req,zoom())

def snakecall():
    snake()
def eyecall(req):
    return render(req,eye())

def home(req):
    return render(req,"home.html")
def vmc(req):
    return render(req,vmCall())

def sg(req):
    return render(req,snakecall())

def fun(req):
    return render(req,ctrl())

def vc(req):
    return render(req,"vc.html")