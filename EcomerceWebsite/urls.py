
from django.contrib import admin
from django.urls import path
from ecomerceApp import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('adminmain/', admin.site.urls),
    path('admin/', views.adminLogin, name="admin-page"),
    path('',views.demoPage, name = "demo-page")
]

#static and media root configurations
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
