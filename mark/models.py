from django.db import models

# Create your models here.
class Ex(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=20)
    user_total = models.CharField(max_length=20)
    user_percent = models.CharField(max_length=20)
    user_division = models.CharField(max_length=20)
   
    def __str__(self):
        return self.user_name

 