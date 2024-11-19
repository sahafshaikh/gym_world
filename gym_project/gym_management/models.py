
from django.db import models
from django.contrib.auth.models import User

class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    membership_type = models.CharField(max_length=50)
    join_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.username

class Trainer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=100)
    experience_years = models.IntegerField()

    def __str__(self):
        return self.user.username

class GymClass(models.Model):
    name = models.CharField(max_length=100)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    schedule = models.DateTimeField()
    max_capacity = models.IntegerField()
    
    def __str__(self):
        return self.name
# Create your models here.
