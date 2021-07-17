"""web_form URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.urls import path,include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from web_app.views import *
from web_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',ManageEmployeeDetails.as_view()),
    path('employee',views.index,name="employee"),
    path('', include,'web_app.views.home', name='home'),
    path('create_form_emeeployee', views.insert, name="create_form_emeeployee"),
    path('update/<int:id>',views.UpdateemployeeGet,name="update"),
    path('emeeploy_update/<int:id>',views.employeeupdate, name="employee_update"),
    path('delete/<int:id>',views.deleteemployeedetails, name="delete"),

]
