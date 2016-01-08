from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import *

class UserProfileInline(admin.StackedInline):
    # list_display = ('user' 'website')
    # search_fields = ['user']
    # form = MyUserChangeForm
    # add_form = MyUserCreationForm
    model=UserProfile
    list_display=['website']
    can_delete = False
    verbose_name_plural = 'UserProfile'
class UserAdmin(BaseUserAdmin):
	BaseUserAdmin.list_display += ('get_website','get_gender','get_date')
	inlines = (UserProfileInline,)
	list_filter = ('username',)
	search_fields = ('username',)
	ordering = ('-is_superuser','-is_active','username')

	def  get_website(self, obj):
		return UserProfile.objects.get(user=obj).website
	def get_gender(self, obj):
		return UserProfile.objects.get(user=obj).gender
	def get_date(self,obj):
		return UserProfile.objects.get(user=obj).holiday_date

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
