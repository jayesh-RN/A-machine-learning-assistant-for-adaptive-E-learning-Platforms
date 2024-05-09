from django.contrib import admin
from contact.models import Contact
class ContactAdmin(admin.ModelAdmin):
    list_display=('fname', 'lname', 'email', 'msg', 'additional')
    
admin.site.register(Contact,ContactAdmin)
# Register your models here.
