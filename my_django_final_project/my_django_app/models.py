from django.db import models

# Create your models here.
class users_info(models.Model): 
    user_name = models.CharField(max_length=100) 
    user_age = models.PositiveIntegerField() 
    user_city = models.CharField(max_length=100) 
    user_email = models.CharField(max_length=100) 

    # def __str__(self):
    #     return f"{self.user_name} {self.user_city} {self.user_age}"

class users_profile(models.Model):
    user_id = models.IntegerField()
    user_name = models.CharField(max_length=100)
    user_age = models.PositiveIntegerField()
    user_city = models.CharField(max_length=100)
    user_email = models.CharField(max_length=100)
    user_image = models.CharField(max_length=200)
                                  
    def _str_(self):
        return f"{self.user_name} {self.user_city} {self.user_age}"