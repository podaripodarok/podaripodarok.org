from django.contrib import admin
from .models import UserPP, Category, SocialAccount, SocialAccountType, Address


admin.site.register(UserPP)
admin.site.register(Category)
admin.site.register(SocialAccount)
admin.site.register(SocialAccountType)
admin.site.register(Address)
