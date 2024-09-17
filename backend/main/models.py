from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
    photo_url = models.CharField(blank=True,max_length=500)
    class Meta :
        constraints = [
            models.UniqueConstraint(fields=['email'],name='unique_active',violation_error_message='user with that email already exists')
        ]

    def to_dict(self):
        return{
            "id":self.id,
            "username":self.username,
            "email":self.email,
            "photo_url":self.photo_url,
            "firstname" : self.first_name,
            "lastname" : self.last_name,
        }
class Owner(models.Model):
    id = models.IntegerField(primary_key = True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def to_dict(self):
        return{
            "id":self.id,
            "user":self.user.to_dict()
        }

class Walker(models.Model):
    id = models.IntegerField(primary_key = True)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.CharField(blank=True,max_length=500)
    rating = models.IntegerField(blank=True,null=True)
    certified = models.BooleanField(null=False)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now = True)

    def to_dict(self):
        return{
            "id":self.id,
            "bio":self.bio,
            "rating":self.rating,
            "certified":self.certified,
            "user":self.user.to_dict()
        }

class Companion(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(null=False,max_length=150)
    owner = models.ForeignKey(Owner,on_delete=models.CASCADE)
    breed = models.CharField(null = False,max_length=50)
    weight = models.FloatField(null = False)
    age = models.IntegerField(null=False)
    companion_notes = models.CharField(blank=True,max_length=500)
    pet_address = models.CharField(null=False,max_length=500)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    def to_dict(self):
        return{
            "id":self.id,
            "breed":self.breed,
            "weight":self.weight,
            "age":self.age,
            "comapanion_notes":self.companion_notes,
            "pet_address":self.pet_address,
            "owner" :self.owner.to_dict(),
            "name" : self.name
        }

class Appointment(models.Model):
    id = models.IntegerField(primary_key=True)
    companion = models.ForeignKey(Companion,null=True,blank=True, on_delete=models.CASCADE)
    appointment_address = models.CharField(blank=True,max_length=500)
    walker = models.ForeignKey(Walker,null=True,blank=True,on_delete=models.CASCADE)
    owner = models.ForeignKey(Owner,null = True,blank=True,on_delete=models.CASCADE)
    start_time = models.DateTimeField(null=True,blank=True)
    end_time = models.DateTimeField(null=True,blank=True)
    status = models.CharField(blank=True,max_length=100)
    appointment_notes = models.CharField(blank=True,max_length=500)
    type = models.CharField(blank=True,max_length=100)
    media_url = models.CharField(blank=True,max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



    def to_dict(self):
        return{
            "id":self.id,
            "companion":self.companion if not self.companion else self.companion.to_dict(),
            "appointment_address":self.appointment_address,
            "walker": self.walker if not self.walker else self.walker.to_dict(),
            "owner":self.owner if not self.owner else self.owner.to_dict(),
            "start_time":self.start_time,
            "end_time":self.end_time,
            "status":self.status,
            "appointment_notes":self.appointment_notes,
            "type":self.type,
            "media_url":self.media_url
        }

class Review(models.Model):
    id = models.IntegerField(primary_key=True)
    author = models.OneToOneField(User,on_delete=models.CASCADE)
    appointment = models.ForeignKey(Appointment,on_delete=models.CASCADE)
    comments = models.CharField(blank=True,max_length=500)
    rating = models.IntegerField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def to_dict(self):
        return{
            "id":self.id,
            "author":self.author.to_dict(),
            "appointment":self.appointment.to_dict(),
            "comments":self.comments,
            "rating":self.rating
        }
