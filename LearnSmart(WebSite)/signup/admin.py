from django.contrib import admin
from signup.models import Register

# Register your models here.
class RegisterAdmin(admin.ModelAdmin):
    list_display=('fname', 'lname', 'email', 'password')
    
admin.site.register(Register,RegisterAdmin)