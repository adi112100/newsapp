from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NewUserForm(UserCreationForm):
    name = forms.CharField( max_length=100,
                            required = True,
                            widget = forms.TextInput(attrs={'placeholder':'Enter your name'}))
    
    email = forms.EmailField(required=True,
                             widget = forms.EmailInput(attrs={'placeholder':'Enter your email'})  )
    
    age = forms.IntegerField(required=True,
                             widget = forms.NumberInput(attrs={'placeholder':'Enter your age'}))
    
    choice = ( 
    ("Male", "Male"), 
    ("Female", "Female"), 
    ) 

    choice1 = ( 
    ("Student", "Student"), 
    ("Engineer", "Engineer"),
    ("Doctor", "Doctor"),
    ("Bussiness", "Bussiness"),
    ("Government servant", "Government servant"),
    ("Other", "Other")
    )
    
    gender = forms.ChoiceField(choices = choice, widget=forms.RadioSelect())
    profession = forms.ChoiceField(choices = choice1)

    class Meta:
        model = User
        fields = ("name", "username", "email", "age", "gender", "profession", "password1", "password2")

class Data:

    def __init__(self,name,username,email,age,gender,profession,password1,password2):
        super().__init__()
        self.name = name
        self.username = username
        self.email = email
        self.age = age
        self.gender = gender
        self.profession = profession
        
