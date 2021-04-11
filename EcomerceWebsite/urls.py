
from django.contrib import admin
from django.urls import path
from ecomerceApp import views,AdminView

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('adminmain/', admin.site.urls),
    path('admin/', views.adminLogin, name="admin-login-page"),
    path('', views.demoPage, name="demo-page"),
    
    #Admin Views
    path('admin_home/', AdminView.admin_home, name="admin-home-page"),
    path('admin_login_proccess/', AdminView.adminLoginProccess, name="admin-login-process"),
    path('admin_logout_proccess/', AdminView.adminLogoutProccess, name="admin-logout-process"),
    #  Category
    path('category_list/', AdminView.CategoriesListView.as_view(), name="category-list-page"),
    path('category_create/', AdminView.CategoriesCreateView.as_view(), name="category-create-page"),
    path('category_update/<slug:pk>', AdminView.CategoriesUpdateView.as_view(), name="category-update-page"),
    #Sub  Category
    path('sub_category_list/', AdminView.SubCategoriesListView.as_view(), name="sub-category-list-page"),
    path('sub_category_create/', AdminView.SubCategoriesCreateView.as_view(), name="sub-category-create-page"),
    path('sub_category_update/<slug:pk>', AdminView.SubCategoriesUpdateView.as_view(), name="sub-category-update-page"),

]

#static and media root configurations
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
