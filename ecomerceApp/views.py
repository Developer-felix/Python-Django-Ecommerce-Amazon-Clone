from django.shortcuts import render

def demoPage(request):
    return render(request,'demo.html')