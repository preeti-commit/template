from django import forms
from .models import *
from web_app.models import *


# class EmployeeForm(forms.Form):
#     employee_name = forms.CharField(required=False)
#     email = forms.CharField(required=False)
#     salary = forms.CharField(required=False)
#     deduction = forms.CharField(required=False)
#     gross_pay = forms.CharField(required=False)
#
#     class Meta:
#         model = Employee
#         fields = (
#             'employee_name',
#             'email',
#             'salary',
#             'deduction',
#             'gross_pay',
#         )



class EmployeeForm(forms.ModelForm):
    gross_pay = forms.CharField(required=False)
    class Meta:
        model = Employee
        fields = (
            'employee_name',
            'email',
            'salary',
            'deduction',
            'gross_pay',
        )

    # def save(self, commit=True):
    #     world = super().save(commit=False)
    #     world.is_location = True
    #     if commit:
    #         world.save()
    #     return world