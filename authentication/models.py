from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # Tambahkan field kustom jika diperlukan
    # Misalnya: photo = models.ImageField(upload_to='profile_photos/', blank=True)
    
    def __str__(self):
        return self.username