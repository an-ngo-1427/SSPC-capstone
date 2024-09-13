from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):

    # id = models.IntegerField(primary_key = True)
    # username = models.CharField(max_length=50)
    # email = models.EmailField(null=False)
    # hashedPassword = models.CharField(max_length=200)
    photo_url = models.CharField(null=True,max_length=500)
    # firstname = models.CharField(null=False,max_length=100)
    # lastname = models.CharField(null=False,max_length=100)
    # created_at = models.DateField()
    # updated_at = models.DateField()

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
    created_at = models.DateField()
    updated_at = models.DateField()

    def to_dict(self):
        return{
            "id":self.id,
            "user":self.user.to_dict()
        }

class Walker(models.Model):
    id =models.IntegerField(primary_key = True)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.CharField(max_length=500)
    rating = models.IntegerField(null=True)
    certified = models.BooleanField(null=False)

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
    walkers = models.ManyToManyField(Walker,related_name='companions')
    owner = models.ForeignKey(Owner,on_delete=models.CASCADE)
    breed = models.CharField(null = False,max_length=50)
    weight = models.FloatField(null = False)
    age = models.IntegerField(null=False)
    companion_notes = models.CharField(null=True,max_length=500)
    pet_address = models.CharField(null=False,max_length=500)
    created_at = models.DateField()
    updated_at = models.DateField()

    def to_dict(self):
        return{
            "id":self.id,
            "breed":self.breed,
            "weight":self.weight,
            "age":self.age,
            "comapanion_notes":self.companion_notes,
            "pet_address":self.pet_address,
            "owner" :self.owner.to_dict(),
            "walkers" : [walker.to_dict() for walker in self.walkers]
        }

class Appointment(models.Model):
    id = models.IntegerField(primary_key=True)
    companion = models.ForeignKey(Companion, on_delete=models.CASCADE)
    appointment_address = models.CharField(max_length=500)
    walker = models.ForeignKey(Walker,on_delete=models.CASCADE)
    owner = models.ForeignKey(Owner,on_delete=models.CASCADE)
    start_time = models.DateField(null=False)
    end_time = models.DateField(null=False)
    status = models.CharField(null=False,max_length=100)
    appointment_notes = models.CharField(null=True,max_length=500)
    type = models.CharField(null=False,max_length=100)
    media_url = models.CharField(null=True,max_length=500)

    def to_dict(self):
        return{
            "id":self.id,
            "companion_id":self.companion,
            "appointment_address":self.appointment_address,
            "walker": self.walker.to_dict(),
            "owner":self.owner.to_dict(),
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
    comments = models.CharField(max_length=500)
    rating = models.IntegerField(null=False)
    created_at = models.DateField()
    updated_at = models.DateField()

    def to_dict(self):
        return{
            "id":self.id,
            "author":self.author.to_dict(),
            "appointment":self.appointment.to_dict(),
            "comments":self.comments,
            "rating":self.rating
        }
