from django import forms
from django.forms import ModelForm
from polls.models import Recipes, comments
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User

class Edit_recipe_form(ModelForm):
    class Meta:
        model=Recipes
        fields=['name','description','duration','image']


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update({"class":"shadow appearance-none border rounded py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline w-full"})
        self.fields["description"].widget.attrs.update({"class":"shadow appearance-none border rounded py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline w-full"})
        self.fields["duration"].widget.attrs.update({"class":"shadow appearance-none border rounded py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline w-full"})
        self.fields["image"].widget.attrs.update({"class":"shadow appearance-none border rounded py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline w-full"})
       



class create_recipe_form(ModelForm):
    class Meta:
        model=Recipes
        fields=['name','description','duration','image']


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update({"class":"shadow appearance-none border rounded py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline w-full"})
        self.fields["description"].widget.attrs.update({"class":"shadow appearance-none border rounded py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline w-full"})
        self.fields["duration"].widget.attrs.update({"class":"shadow appearance-none border rounded py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline w-full"})
        self.fields["image"].widget.attrs.update({"class":"shadow appearance-none border rounded py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline w-full"})
       



class register_form(UserCreationForm):


    class Meta:
        model=User
        fields=["username","email"]



    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({"class":"shadow appearance-none border rounded py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline w-full"})
        self.fields["email"].widget.attrs.update({"class":"shadow appearance-none border rounded py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline w-full"})
        self.fields["password1"].widget.attrs.update({"class":"shadow appearance-none border rounded py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline w-full"})
        self.fields["password2"].widget.attrs.update({"class":"shadow appearance-none border rounded py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline w-full"})
       
       




class commentForm(ModelForm):
    class Meta:
        model=comments
        fields=['comments']


    def __init__(self, *args , **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['comments'].widget.attrs.update({"class":"shadow appearance-none border rounded py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline w-full","placeholder":"ecrire votre commentaire "})

    
   
