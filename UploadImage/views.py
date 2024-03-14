from django.shortcuts import render
from django.http import HttpResponse

def Index(request):
    return render(request,r"D:\6thsem\project\project\templates\index.html")
# def Index(request):
#     return HttpResponse(req,"asdasd")