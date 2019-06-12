from django.db import models
from django.contrib.auth.models import User
#from django.core.validators import RegexValidator


class UserPP(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    middle_name = models.CharField(max_length=30, blank=True, default='')
    address = models.CharField(max_length=500, blank=True, default='')
    #phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
    #                             message="Phone number must be entered in the format: '+x xxx xxx xx xx'. Up to 15 digits allowed.")
    #phone_number = models.CharField(validators=[phone_regex], max_length=15, blank=False)
    phone_number = models.CharField(max_length=15, blank=False)
    week_show_count = models.IntegerField(blank=True, default=0)

    def publish(self):
        self.save()

    def __str__(self):
        return str(self.user)

    class Meta:
        ordering = ('user',)


class Category(models.Model):
    """ Describes different activities person can participates"""
    users = models.ManyToManyField(UserPP)
    name = models.CharField(max_length=30, blank=True, default='')
    description = models.CharField(max_length=30, blank=True, default='')

    def publish(self):
        self.save()

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ('name',)


class Family(models.Model):
    userPP = models.OneToOneField(UserPP, on_delete=models.CASCADE)

    def publish(self):
        self.save()

    def __str__(self):
        return str(self.userPP)

    class Meta:
        ordering = ('userPP',)

         
class Volunteer(models.Model):
    userPP = models.OneToOneField(UserPP, on_delete=models.CASCADE)

    def publish(self):
        self.save()

    def __str__(self):
        return str(self.userPP)

    class Meta:
        ordering = ('userPP',)        
     

class Giver(models.Model):
    userPP = models.OneToOneField(UserPP, on_delete=models.CASCADE)

    def publish(self):
        self.save()

    def __str__(self):
        return str(self.userPP)

    class Meta:
        ordering = ('userPP',)    


class SocialAccountType(models.Model):
    """Social network name"""
    social_account_name = models.CharField(max_length=100, blank=True, default='')
        

    def publish(self):
        self.save()

    def __str__(self):
        return str(self.social_account_name)

    class Meta:
        ordering = ('social_account_name',)


class SocialAccount(models.Model):
    """To keep social network tokens"""
    userPP = models.ForeignKey(UserPP)
    social_account_type_id = models.ForeignKey(SocialAccountType)
    social_account_token = models.CharField(max_length=100, blank=True, default='')
    

    def publish(self):
        self.save()

    def __str__(self):
        return str(self.social_account_token)

    class Meta:
        ordering = ('social_account_token',)
