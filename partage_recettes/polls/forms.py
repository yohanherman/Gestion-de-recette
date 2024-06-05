from django import forms
from django.forms import ModelForm
from polls.models import Recipes, comments
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Edit_recipe_form(ModelForm):
    class Meta:
        model=Recipes
        fields=['name','description','duration']


class create_recipe_form(ModelForm):
    class Meta:
        model=Recipes
        fields=['name','description','duration']




class register_form(UserCreationForm):

    # username= forms.CharField(widget=forms.TextInput(attrs={
    #     'class':'input',
    #     'type':'text',
    #     'placehorder':'saisissez votre identifiant'
    # }))



    # email=forms.CharField(widget=forms.TextInput(attrs={
    #     'class':'input',
    #     'type':'email',
    #     'placeholder':'saisissez votre email'
    # }))


    
    class Meta:
        model=User
        fields=["username","email"]



class commentForm(ModelForm):
    class Meta:
        model=comments
        fields=['comments']

    
   
