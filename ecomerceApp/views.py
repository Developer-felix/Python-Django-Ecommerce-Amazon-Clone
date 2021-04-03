from django.shortcuts import render

def demoPage(request):
    return render(request, 'demo.html')


def adminLogin(request):
    return render(request,'admin_templates/signin.html')