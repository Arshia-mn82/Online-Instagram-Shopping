from django.contrib.admin import register,ModelAdmin

from accounts.models import UserProfile

@register(UserProfile)
class UserProfileAdmin(ModelAdmin):
    pass


