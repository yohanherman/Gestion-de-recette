from django.contrib import admin
from polls.models import Recipes, comments


class pageAdmin(admin.ModelAdmin):
    list_display=['name','description','duration', 'created_date','updated_date','user_id']



@admin.register(comments)
class CommentAdmin(admin.ModelAdmin):
    list_display=['comments','recipe_id','user_id']




admin.site.register(Recipes,pageAdmin)

