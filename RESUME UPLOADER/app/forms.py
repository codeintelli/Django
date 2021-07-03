from django import forms
from .models import Resume

GENDER_CHOICES = [
    ('Male','Male'),
    ('Female','Female'),
    ('Rather Not Say','Rather Not Say')
]
JOB_CITY_CHOICES = [
    ('Delhi','Delhi'),
    ('Pune','Pune'),
    ('Ranchi','Ranchi'),
    ('Gujarat','Gujarat'),
    ('Banglore','Banglore'),
]


class ResumeForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget = forms.RadioSelect)
    job_city = forms.MultipleChoiceField(label='Prefered Job Location',choices=JOB_CITY_CHOICES, widget = forms.CheckboxSelectMultiple)
    class Meta:
        model = Resume
        fields = ['name','dob','gender','locality','city','pin','state','mobile','email','job_city','profile_image','my_file']
        labels = {
            'name':'Full Name',
            'dob':'Date Of Birth',
            'pin':'Pin Code',
            'Mobile': 'Contact Number',
            'email':'Email Id',
            'profile_image':'Profile Image',
            'my_file':'Document',

        }

        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'dob':forms.DateInput(attrs={'class':'form-control','id':'datepicker'}),
            'locality':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'pin':forms.NumberInput(attrs={'class':'form-control'}),
            'state':forms.Select(attrs={'class':'form-control'}),
            'mobile':forms.NumberInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
        }