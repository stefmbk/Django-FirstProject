from django.urls import include, path
from django.contrib import admin
from . import views

app_name = 'mainapp'
urlpatterns = [
    path('', views.findjob, name='index'),
    path('findjob/', views.findjob, name='findjob'),
    path('postjob/', views.addCompany, name='addCompany'),
    path('postjob/<int:company_id>/', views.postJob, name='postJob'),
    path('findjob/<int:job_id>/', views.jobdetail, name='jobdetail'),
    path('findjob/<int:job_id>/apply', views.apply, name='apply'),
    path('company/<int:company_id>/', views.companydetail, name='companydetail'),
   # path('admin/', admin.site.urls,name='admin'),
    ]