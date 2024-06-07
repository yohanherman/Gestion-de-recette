from django.shortcuts import get_object_or_404, redirect, render
from polls.models import Recipes,comments
from django.contrib.auth.models import User
from polls.forms import Edit_recipe_form,create_recipe_form ,register_form,commentForm
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm,PasswordResetForm
from django.contrib.auth import authenticate,login,logout,get_user_model
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes,force_str
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from polls.token import account_activation_token
from django.contrib import messages
from django.core.mail import EmailMessage
from django.contrib.auth.decorators import login_required
import os

def homePage(request):
    return render(request,'core/homepage.html',{'text':"je suis la page d'accueil"})


def get_all_recipes(request):
    every_user_recipes = Recipes.objects.select_related('user').all().exclude(user=request.user)
    
    return render(request, 'core/UsersRecipes.html', {'every_user_recipes': every_user_recipes})


@login_required
def get_user_recipes(request):
    fast_recipes = Recipes.objects.select_related('user').filter(duration = 15 ).exclude(user=request.user)
    if request.user.is_authenticated:
        recipes = Recipes.objects.filter(user=request.user)

    else:
        recipes = Recipes.objects.none() 
        


    context={'recipes': recipes,
             'fast_recipes':fast_recipes
     }
    
    return render(request, 'core/recipes.html', context)


def get_single_recipes2(request,id):
        detailsrecipe = get_object_or_404(Recipes,id=id)
        get_comments = detailsrecipe.comments.all()
        number_comments = detailsrecipe.comments.count()
        context={'detailsrecipe': detailsrecipe,
                 'get_comments':get_comments,
                 'number_comments': number_comments
         }
        
        return render(request,'core/detailOtherRecipe.html', context)


@login_required
def get_single_recipes(request,id):
        detailsrecipe = get_object_or_404(Recipes,id=id,user=request.user)

        return render(request,'core/detailedRecipe.html',{'detailsrecipe': detailsrecipe})


@login_required
def edit_recipe(request,id):
    detailsrecipe = get_object_or_404(Recipes,id=id)
    if request.method == 'POST':
        form = Edit_recipe_form(request.POST ,request.FILES , instance=detailsrecipe)
        if form.is_valid():
            if 'image' in request.FILES:
                if detailsrecipe.image and detailsrecipe.image.name != 'assiete_vide.jpg':
                
                    if os.path.isfile(detailsrecipe.image.path):  # cette fonction me permet de verifier que mon image existe dans mon os
                        os.remove(detailsrecipe.image.path)
                detailsrecipe.image = request.FILES['image']

            form.save()
            messages.success(request, 'recette modfiéé avec succès')
            return redirect('detailedRecipe', id=id)

    else:
        form=Edit_recipe_form(instance=detailsrecipe)

    return render(request, 'core/edit.html', {'form': form})


@login_required
def create_recipe(request):
    if request.method == 'POST':
        creation_form=create_recipe_form(request.POST)
        if creation_form.is_valid():
            recipe = creation_form.save(commit=False)
            recipe.user=request.user
            recipe.save()

            messages.success(request, 'Recette ajouteé avec succes')
            # print('ajouteé')
            return redirect('Recipes')

    else:
        creation_form=create_recipe_form()

    return render(request,'core/createRecipe.html', {'creation_form': creation_form })



@login_required
def delete_confirmation(request,id):
     recipe = get_object_or_404(Recipes, id=id)

     return render (request,'core/deleteConfirmation.html', {'recipe': recipe})


@login_required
def delete_recipe(request,id):
    recipe = get_object_or_404(Recipes, id=id)
    recipe.delete()
    # print(' bien effacée')
    messages.success(request,'recette effacée avec succes')

    return redirect('Recipes')


def login_user(request):
    if request.method == 'POST':
        # email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(request , username = username, password = password)

        if user is not None:
            login(request,user)
            # print(user)
            return redirect('Recipes')
        else:
            messages.error(request, 'Email/mot de passe incorrect')

    login_form = AuthenticationForm()

    return render(request, 'core/login.html',{'login_form' : login_form })


def logout_user(request):
    logout(request)
    messages.info(request, "Deconnexion reussie")
    return redirect('homepage')


def activate(request, uidb64,token):
    User=get_user_model()
    try:
        uid=force_str(urlsafe_base64_decode(uidb64))
        user=User.objects.get(pk=uid)
    except:
        user = None


    if user is not None and account_activation_token.check_token(user,token):
        user.is_active =True
        user.save()

        messages.success(request,'Thank you for your Email confirmation , now you can login your account')
        return redirect('login')
    else:
        messages.error(request,'Activation link is invalid')

    return redirect('homepage')



def activeEmail(request, user ,to_email):
    mail_subject=" Activate your user account"
    message = render_to_string("core/template_account_activation_email.html",{
        'user':user,
        'domain':get_current_site(request).domain,
        'uid':urlsafe_base64_encode(force_bytes(user.pk)),
        'token':account_activation_token.make_token(user),
        'protocol':'https' if request.is_secure() else 'http'
    })
    email = EmailMessage(mail_subject,message,to=[to_email])
    if email.send():
         messages.success(request, f'Dear {user} , please go to your email {to_email} inbox and click on \ received activation link to confirm and complete the registration. Note: Check your spam folder ')

    else:
        messages.error(request, f'Problem sending email to {to_email} check if you typed it correctly.')



def signup_user(request):
    if request.method == 'POST':
        form=register_form(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.is_active = False
            user.save()
            activeEmail(request, user,form.cleaned_data.get('email'))
            return redirect('homepage')
    else:
        form = register_form()

    return render(request, 'core/signup.html', {'form': form})



def get_all_members(request):
    all_members = User.objects.all()
    return render(request, 'core/members.html',{'all_members': all_members})


@login_required
def send_comments(request,id):
    if request.method=='POST':
        comment_form = commentForm(request.POST)
        if comment_form.is_valid():
            comments= comment_form.save(commit=False)
            comments.recipe = Recipes.objects.get(id=id)
            comments.user=request.user
            comments.save()
            messages.success(request, 'votre commentaire a bien été enregistré')
            return redirect('detailedRecipeOtherUser' , id=id )
        
    else:
        comment_form = commentForm()
        
    return render(request,'core/createComments.html',{'comment_form' : comment_form })




# def display_comments(request,id,recipe):
#     detailsrecipe = get_object_or_404(Recipes, id=id)
#     comments = recipe.comments.all()

#     context={'the_comments': the_comments,
#              'detailsrecipe':detailsrecipe
        
#     }
             
#     return render(request,'core/detailOtherRecipe.html',context)



# def display_comments(request,recipe_id):
#     recipe = get_object_or_404(Recipes, id=recipe_id)
#     comments = recipe.comments.all()

#     context={'comments': comments,
#              'recipe':recipe
        
#     }
             
#     return render(request,'core/detailOtherRecipe.html',context)


             