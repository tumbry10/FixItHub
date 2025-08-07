from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        (1, 'SystAdmin'),
        (2, 'SystUser'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='user')

    class Meta:
        db_table = 'users'
    
    def __str__(self):
        return self.username
    
class SystAdmin(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'syst_admin'

    def __str__(self):
        return f"SystAdmin: {self.user.username}"

class SystUser(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'syst_user'

    def __str__(self):
        return f"SystUser: {self.user.username}"
    
class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures', blank=True, null=True)

    class Meta:
        db_table = 'user_rofile'

    def __str__(self):
        return f"{self.user.username}'s Profile"
