from django.contrib import messages
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views import View
from .models import Employee


def index(request):
    return render(request,'form.html',{'index': Employee.objects.all()})


def insert(request):
    if request.method == 'POST':
        deduction = request.POST.get('deduction')
        salary = request.POST.get('salary')
        grs = int(salary)-int(deduction)
        emp =Employee(employee_name=request.POST.get('employee'),
                email=request.POST.get('email'),
                salary=request.POST.get('salary'),
                deduction=request.POST.get('deduction'),
                gross_pay=grs,)
        emp.save()
    return redirect('/')


def UpdateemployeeGet(request, id):
    template_name = 'update_form.html'
    emp_info = Employee.objects.get(id=id)
    context = {
        'emp_info':emp_info,
    }
    return render(request, template_name, context)


def employeeupdate(request, id):
    if request.method == 'POST':
        emp = Employee.objects.get(id=id)
        deduction = request.POST.get('deduction')
        salary = request.POST.get('salary')
        grs = int(salary) - int(deduction)
        emp.employee_name=request.POST.get('employee')
        emp.email=request.POST.get('email')
        emp.salary=request.POST.get('salary')
        emp.deduction=request.POST.get('deduction')
        emp. gross_pay=grs
        emp.save()
        return redirect('/')




class ManageEmployeeDetails(View):
    template_name = 'form_details.html'

    def get(self, request):
        query_set = Employee.objects.all().order_by('-pk')
        context = {
            'employe_detail': query_set,
        }
        return render(request, self.template_name, context)


def deleteemployeedetails(request, id):
    empl = Employee.objects.filter(id=id)
    empl.delete()
    return redirect('/')
