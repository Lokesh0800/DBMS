from django import forms
from django.forms import ModelForm
from empapp.models import *

class empform(ModelForm):
    class Meta:
        model = Employees
        fields = "__all__"
        labels = {
            'Empname':'',
            'Designation':'',
            'Department':'',
            'DOJ':'',
            'Salary':'',
            'Contact':'',
        }
        
        widgets={
            'Empname':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter name'}),
            'Designation':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Position'}),
            'Department':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Department'}),
            'DOJ':forms.DateInput(attrs={'class':'form-control','placeholder':'Enter DOJ','type':'date'}),
            'Salary':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter salary'}),
            'Contact':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Contact'}),
        }

class departmentform(ModelForm):
    class Meta:
        model = Department
        fields = "__all__"
        status = (
            ('Active','Active'),
            ('Inactive','Inactive')
        )
        labels = {
            'Department_name':'',
            'Status':'',
        }
        
        widgets = {
            "Department_name": forms.TextInput(attrs={'class':'form-control'}),
            "Status": forms.Select(choices=status,attrs={'class':'form-control'}),
        }

class clientform(ModelForm):
    class Meta:
        model = Client
        fields = "__all__"
        labels = {
            "Client_name": '',
            "Company_name" : '',
            "Company_address" : '',
            "Company_contact" : '',
            "Company_email" : '',
            "Company_website" : '',
            "Service_opted" : '',
            "Service_status" : '',
        }
        
        widgets = {
            'Client_name': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Client name'}),
            'Company_name' : forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Company name'}),
            'Company_address' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Comapny address'}),
            'Company_contact' : forms.TextInput(attrs={'class':'form-control','placeholder':'Enter contact'}),
            'Company_email' : forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter email'}),
            'Company_website' : forms.URLInput(attrs={'class':'form-control','placeholder':'Enter company website'}),
            'Service_opted' : forms.TextInput(attrs={'class':'form-control','placeholder':'Choose service'}),
            'Service_status' : forms.TextInput(attrs={'class':'form-control'}),
        }