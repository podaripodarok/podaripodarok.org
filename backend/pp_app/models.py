from django.db import models
from django.contrib.auth.models import User
#from django.core.validators import RegexValidator
from django.core.validators import MaxValueValidator, MinValueValidator


class Address(models.Model):
    user = models.OneToOneField(User, default=None, on_delete=models.CASCADE)
    post_index = models.IntegerField(blank=True, default=None, 
        validators=[MaxValueValidator(999999), MinValueValidator(100000)])
    region = models.CharField(max_length=1024, blank=True, default='')
    district = models.CharField(max_length=1024, blank=True, default='')
    inhabited_locality = models.CharField(max_length=1024, blank=True, default='') #
    street = models.CharField(max_length=1024, blank=True, default='')
    building_number = models.IntegerField(blank=True, default=0)
    building_structure = models.CharField(max_length=1024, blank=True, default='')
    flat_number = models.IntegerField(blank=True, default=0)
    stage = models.IntegerField(blank=True, default=0)
    intercome_code = models.CharField(max_length=30, blank=True, default='')

    def publish(self):
        self.save()

    def __str__(self):
        return str(self.user)

    class Meta:
        ordering = ('inhabited_locality', 'street',)

class UserPP(models.Model):
    user = models.OneToOneField(User, default=None, on_delete=models.CASCADE)
    middle_name = models.CharField(max_length=30, blank=True, default='')
    phone_number = models.CharField(max_length=15, blank=False)
    #phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
    #                             message="Phone number must be entered in the format: '+x xxx xxx xx xx'. Up to 15 digits allowed.")
    #phone_number = models.CharField(validators=[phone_regex], max_length=15, blank=False)
    address = models.OneToOneField(Address, default=None, on_delete=models.SET_DEFAULT)
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


class SocialAccountType(models.Model):
    """Social network name"""
    name = models.CharField(max_length=100, blank=True, default='')
        

    def publish(self):
        self.save()

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ('name',)


class SocialAccount(models.Model):
    """To keep social network tokens"""
    userPP = models.ForeignKey(UserPP, on_delete=models.CASCADE)
    social_account_type_id = models.ForeignKey(SocialAccountType, on_delete=models.CASCADE)
    token = models.CharField(max_length=100, blank=True, default='')
    

    def publish(self):
        self.save()

    def __str__(self):
        return str(self.token)

    class Meta:
        ordering = ('token',)

