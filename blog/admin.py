from django.contrib import admin
from .models import HomePage, AboutPage , ContactPage ,Post , Comment , Contact

# Register your models here.

admin.site.register(HomePage)
admin.site.register(AboutPage)
admin.site.register(ContactPage)
admin.site.register(Contact)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','slug','auther','created_at','status']
    list_filter = ['status','created_at','publish','auther']
    search_fields = ['title','body']
    prepopulated_fields = {'slug':('title', )}
    raw_id_fields = ['auther']
    date_hierarchy = 'publish'
    ordering = ['status','publish']
    
    
@admin.register(Comment)
class commentAdmin(admin.ModelAdmin):
    list_display = ['name','email','created_at','active','body']
    list_filter = ['active','created_at']
    search_fields = ['name','body','active']
    
    