
from django.contrib import admin
from django.urls import include, path
from polls import views

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homePage,name="homepage"),

    path('All-Recipes/', views.get_all_recipes,name="all_users_Recipes"),
    path('Recipes/', views.get_user_recipes , name="Recipes"),
    path('Recipes/<int:id>/',views.get_single_recipes, name='detailedRecipe'),
    path('All-Recipes/<int:id>/',views.get_single_recipes2, name='detailedRecipeOtherUser'),

    path('Recipes/edit/<int:id>/', views.edit_recipe , name='editRecipe'),
    path('create_recipe/',views.create_recipe, name='createRecipe' ),
    path('Recipe/ConfirmationDelete/<int:id>/', views.delete_confirmation ,name='deleteConfirmation'),
    path('Recipes/delete/<int:id>/',views.delete_recipe, name='delete'),

    path('account/login', views.login_user, name ='login'),
    path('account/signup',views.signup_user , name='signup'),
    path('account/logout',views.logout_user ,name='logout'),
    path('activate/<uidb64>/<token>', views.activate ,name='activate'),

    path('members', views.get_all_members, name ='members'),

    path('comments-creation/<int:id>',views.send_comments ,name='comment-creation'),

    # tailwind reloading
    path("__reload__/", include("django_browser_reload.urls")),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
