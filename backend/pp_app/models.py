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
    users = models.ManyToManyField(UserPP)
    name = models.CharField(max_length=30, blank=True, default='')
    description = models.CharField(max_length=30, blank=True, default='')

    def publish(self):
        self.save()

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ('name',)




