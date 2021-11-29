"""academic_performance URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url

from academic import views as academic_views
urlpatterns = [
    url('admin/', admin.site.urls),

    url(r'^$', academic_views.index, name='index' ),

    url(r'^about/$', academic_views.about, name='about' ),

    url(r'^services/$', academic_views.services, name='services' ),

    url(r'^login/$', academic_views.login, name='login' ),

    url(r'^flogin/$', academic_views.flogin, name='flogin' ),

    url(r'^slogin/$', academic_views.slogin, name='slogin' ),

    url(r'^contact/$', academic_views.contact, name='contact' ),

    url(r'^AdminHome/$', academic_views.AdminHome, name='AdminHome'),

    url(r'^FacultyHome/$', academic_views.FacultyHome, name='FacultyHome'),

    url(r'^StudentHome/$', academic_views.StudentHome, name='StudentHome'),

    url(r'^AddFaculty/$', academic_views.AddFaculty, name='AddFaculty'),

    url(r'^ViewFaculty/$',academic_views.ViewFaculty,name='ViewFaculty'),

    url(r'^update/(?P<f_id>\w+)',academic_views.update_faculty),

    url(r'^delete/(?P<f_id>\w+)',academic_views.delete_faculty),
    
    

    url(r'^deleteInternalMarks/(?P<i_id>\w+)',academic_views.deleteInternalMarks),

    url(r'^AddStudent/$', academic_views.AddStudent, name='AddStudent'),

    url(r'^ViewAddStudent/$',academic_views.ViewStudent,name='ViewStudent'),

    url(r'^updateStudent/(?P<s_id>\w+)',academic_views.update_student),

    url(r'^deleteStudent/(?P<s_id>\w+)',academic_views.delete_student),
    
    url(r'^AddInternalMarks/$', academic_views.AddInternalMarks, name='AddInternalMarks'),
    
    url(r'^ViewInternalMarks/$', academic_views.ViewInternalMarks, name='ViewInternalMarks'),
   
    url(r'^PredictStatus/$', academic_views.PredictStatus, name='PredictStatus'),
   
    url(r'^updateInternalMarks/(?P<i_id>\w+)',academic_views.update_internal),
   
    url(r'^ViewPassPredict/$', academic_views.ViewPassPredict, name='ViewPassPredict'),

    url(r'^ViewMarksPredict/$', academic_views.ViewMarksPredict, name='ViewMarksPredict'),
    
    
    url(r'^ViewMarksCNS/$', academic_views.ViewMarksCNS, name='ViewMarksCNS'),
    
    url(r'^ViewMarksUML/$', academic_views.ViewMarksUML, name='ViewMarksUML'),
    
    url(r'^ViewMarksMC/$', academic_views.ViewMarksMC, name='ViewMarksMC'),
    
    url(r'^ViewMarksSTM/$', academic_views.ViewMarksSTM, name='ViewMarksSTM'),
    
    url(r'^ViewMarksHBD/$', academic_views.ViewMarksHBD, name='ViewMarksHBD'),
    

    url(r'^Vsmarks/$', academic_views.Vsmarks, name='Vsmarks'),
    
    
   
]
