from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Categories
from django.views.generic import CreateView, DeleteView, ListView, DetailView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin

class CategoriesListView(ListView):
    model = Categories
    template_name = "admin_templates/category_list.html"

class CategoriesCreateView(SuccessMessageMixin,CreateView):
    model = Categories
    success_message = "Category Added"
    fields = "__all__"
    template_name = "admin_templates/category_create.html"


@login_required(login_url="/admin/")
def admin_home(request):
    return render(request, 'admin_templates/home.html')


def adminLoginProccess(request):
    username = request.POST.get("username")
    password = request.POST.get("password")

    user = authenticate(request=request, username=username, password=password)
    if user is not None:
        login(request=request, user=user)
        return HttpResponseRedirect(reverse("admin-home-page"))
    else:
        messages.error(request, "Error in login! Invalid Login Details!")
        return HttpResponseRedirect(reverse("admin-login-page"))
    return render(request, 'admin_templates/home.html')

def adminLogoutProccess(request):
    logout(request)
    messages.success(request, "Logout Successfully! ")
    return HttpResponseRedirect(reverse("admin-login-page"))
