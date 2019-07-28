from django.db import models
from django.contrib.auth.models import User
#from django.core.validators import RegexValidator
from django.core.validators import MaxValueValidator, MinValueValidator
from enum import Enum


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


class Follower(models.Model):
    """To permit quick access to family or to giver. """
    user_from = models.ForeignKey(UserPP, on_delete=models.CASCADE, related_name='follower')
    user_to = models.ForeignKey(UserPP, on_delete=models.CASCADE, related_name='aim')

    def publish(self):
        self.save()

    def __str__(self):
        return str(f'{self.user_from} - {user_to}')

    class Meta:
        ordering = ('user_from','user_to')


class Responsible(models.Model):
    """Responsible volunteer"""
    user_from = models.ForeignKey(UserPP, on_delete=models.CASCADE, related_name='responsible')
    user_to = models.ForeignKey(UserPP, on_delete=models.CASCADE, related_name='recipient')

    def publish(self):
        self.save()

    def __str__(self):
        return str(f'{self.user_from} - {user_to}')

    class Meta:
        ordering = ('user_from','user_to')


class Action(models.Model):
    """Who participates in action"""
    userPP = models.ManyToManyField(UserPP)
    name = models.CharField(max_length=100, blank=True, default='')
    description = models.CharField(max_length=100, blank=True, default='')
    startDate = models.DateField(("Date"), auto_now=False, auto_now_add=False)
    endDate = models.DateField(("Date"), auto_now=False, auto_now_add=False)

    def publish(self):
        self.save()

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ('name',)


class GifttypeChoice(Enum):   # A subclass of Enum
    SUGGESTION = "Suggestion"
    REQUEST = "Request"


class MeasureChoice(Enum):   # A subclass of Enum
    RUBBLES = "руб."
    UNITS = "шт."
    LITRES = "литр(ов)"
    KILOS = "кг"
    METRES = "метр(ов)"
    HOURS = "час(ов)"


class GiftLabel(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')


class Gift(models.Model):
    """Who participates in action"""
    userPP = models.ManyToManyField(UserPP)
    action = models.ForeignKey(Action, on_delete=models.CASCADE)
    gift_label = models.ManyToManyField(GiftLabel)
    name = models.CharField(max_length=100, blank=True, default='')
    description = models.CharField(max_length=100, blank=True, default='')
    gift_type = models.CharField(
      max_length=100,
      choices=[(tag, tag.value) for tag in GifttypeChoice]  # Choices is a list of Tuple
    )
    measure_type = models.CharField(
      max_length=100,
      choices=[(tag, tag.value) for tag in MeasureChoice]  # Choices is a list of Tuple
    )
    value = models.IntegerField(blank=True, default=1)
    accept_gift_time = models.DateField(("Date"), auto_now=False, auto_now_add=False)

    def publish(self):
        self.save()

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ('name',)













