from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator
from django_countries.fields import CountryField

# Create your models here.

class CustomUser(AbstractUser):
    username = models.CharField(max_length=100)
    email = models.EmailField("email address", blank=False, null=False, unique=True)
    FEMALE = 'F'
    MALE = 'M'
    GENDER_CHOICES = [
        (FEMALE, 'Female'),
        (MALE, 'Male')
    ]
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES, blank=True)
    mobile = models.PositiveIntegerField(blank=True, null=True, validators=[MaxValueValidator(999999999999)])
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return f'{self.email}'

class SocialNetwork(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    site_name = models.CharField(max_length=50, blank=True, null=True)
    site_url = models.URLField(max_length=2000, blank=True, null=True, unique=True)

    def __str__(self):
        return f"{self.site_name}"

class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    email_address = models.EmailField(max_length= 255, blank=True, null=True)
    mobile = models.PositiveIntegerField(blank=True, null=True, validators=[MaxValueValidator(999999999999)])
    phone = models.PositiveIntegerField(blank=True, null=True, validators=[MaxValueValidator(999999999999)])
    country = CountryField(blank=True)
    birth_date = models.DateField(blank=True, null=True)
    image = models.ImageField(upload_to='profile_pics', default='default.jpg')
    social_sites = models.ManyToManyField(SocialNetwork)

    def __str__(self):
        return f"{self.user.email}'s Profile"

