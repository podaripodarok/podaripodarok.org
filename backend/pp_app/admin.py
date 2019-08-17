from django.contrib import admin
from .models import (Address, UserPP, Category, SocialAccountType, SocialAccount, 
Follower, Responsible, Action, GiftLabel, Gift, GiftChild, Message)

admin.site.register(Address)
admin.site.register(UserPP)
admin.site.register(Category)
admin.site.register(SocialAccountType)
admin.site.register(SocialAccount)
admin.site.register(Follower)
admin.site.register(Responsible)
admin.site.register(Action)
admin.site.register(GiftLabel)
admin.site.register(Gift)
admin.site.register(GiftChild)
admin.site.register(Message)