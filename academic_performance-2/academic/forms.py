from django import forms

from .models import AddFaculty_Model,AddStudent_Model,Internal_Model

class AddFaculty_ModelCreate(forms.ModelForm):
    CHOICES=[('M','Male'),
         ('F','Female')]
    subjects = [
        ('CSE', 'CSE'),
        ('EEE', 'EEE'),
      ]
    states = [
        ('OH', 'OHIO'),
        ('NY', 'NEWYORK'),
        ('FL', 'FLORIDA'),
      ]

    fullname=forms.CharField(label='FullName', widget=forms.TextInput(attrs={'class': "form-control"}))
    email=forms.CharField(label='Email', widget=forms.TextInput(attrs={'class': "form-control"}))
    password=forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': "form-control"}))
    dob=forms.CharField(label='Date of Birth', widget=forms.widgets.DateInput(attrs={'class': "form-control",'type':"date"}))
    gender=forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    subject = forms.ChoiceField(label='Subject', widget=forms.Select(attrs={'class': "form-control",'type':"date"}), choices=subjects)
    state = forms.ChoiceField(label='State', widget=forms.Select(attrs={'class': "form-control",'type':"date"}), choices=states)
    phone=forms.CharField(label='Phone', widget=forms.TextInput(attrs={'class': "form-control"}))
    addr = forms.CharField(widget=forms.Textarea(attrs={'class': "form-control"}))
    class Meta:

        model=AddFaculty_Model

        fields='__all__'

class AddStudent_ModelCreate(forms.ModelForm):
    CHOICES=[('M','Male'),
         ('F','Female')]
    cources = [
        ('CSE', 'CSE'),
        ('EEE', 'EEE'),
      ]
    years = [
        ('2019', '2019'),
        ('2020', '2020'),
        ('2021', '2021'),
        ('2022', '2022'),
        ('2023', '2023'),
      ]
  
    
    states = [
        ('OH', 'OHIO'),
        ('NY', 'NEWYORK'),
        ('FL', 'FLORIDA'),
      ]
    rollno=forms.CharField(label='Rollno', widget=forms.TextInput(attrs={'class': "form-control"}))
    fullname=forms.CharField(label='FullName', widget=forms.TextInput(attrs={'class': "form-control"}))
    email=forms.CharField(label='Email', widget=forms.TextInput(attrs={'class': "form-control"}))
    password=forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': "form-control"}))
    dob=forms.CharField(label='Date of Birth', widget=forms.widgets.DateInput(attrs={'class': "form-control",'type':"date"}))
    gender=forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    course = forms.ChoiceField(label='Course', widget=forms.Select(attrs={'class': "form-control"}), choices=cources)
    year = forms.ChoiceField(label='Year', widget=forms.Select(attrs={'class': "form-control"}), choices=years)
    state = forms.ChoiceField(label='State', widget=forms.Select(attrs={'class': "form-control"}), choices=states)
    phone=forms.CharField(label='Phone', widget=forms.TextInput(attrs={'class': "form-control"}))
    addr = forms.CharField(widget=forms.Textarea(attrs={'class': "form-control"}))
    class Meta:

        model=AddStudent_Model

        fields='__all__'

class Internal_ModelCreate(forms.ModelForm):
  
  cns=forms.IntegerField(label='Cryptography', min_value=0,max_value=100)

  uml=forms.IntegerField(label='Uml Design', min_value=0,max_value=100)

  mc=forms.IntegerField(label='Mobile Computing', min_value=0,max_value=100)

  stm=forms.IntegerField(label='Software Testing', min_value=0,max_value=100)

  hbd=forms.IntegerField(label='Hadoop Big Data', min_value=0,max_value=100)

  attendance=forms.IntegerField(label='attendance', min_value=0,max_value=100)


  class Meta:

    model=Internal_Model

    fields='__all__'

