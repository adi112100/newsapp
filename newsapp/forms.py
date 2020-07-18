from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    age = forms.IntegerField(required=True)
    choice =( 
    ("Male", "Male"), 
    ("Female", "Female"), 
    ) 

    choice1 =( 
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
        fields = ("username", "email", "age", "gender", "profession", "password1", "password2")

class Data:

    def __init__(self,username,age,gender,profession,password1,password2):
        super().__init__()
        self.username =username
        self.age = age
        self.gender = gender
        self.profession = profession
        
