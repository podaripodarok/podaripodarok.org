from django.contrib import admin
from .models import UserPP, Category, Family, Volunteer, Giver, SocialAccount, SocialAccountType


admin.site.register(UserPP)
admin.site.register(Category)
admin.site.register(Family)
admin.site.register(Volunteer)
admin.site.register(Giver)
admin.site.register(SocialAccount)
admin.site.register(SocialAccountType)
