from django.shortcuts import render
from django.views import View
from django.http import JsonResponse,HttpResponse
from .models import Appointment,Companion,User,Owner,Walker
from django.views.decorators.csrf import ensure_csrf_cookie
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate, login,logout
from django.db import IntegrityError
from django.core.exceptions import ValidationError
from .validations.UserForm import UserForm
import json
from django.core.serializers import serialize
# Create your views here.
@ensure_csrf_cookie
def getCsurf(request):
    cookies = request.COOKIES.get('csrftoken')
    response = JsonResponse({'csrfToken':cookies})
    return response

def signUp(request):
    userForm = UserForm(request.POST)
    if(not userForm.is_valid()):
        errObj = {}
        errors = userForm.errors.as_data()
        for field,error in errors.items():
            print(error[0])
            errObj[field] = error[0].message
        return JsonResponse({'error':errObj},status=400)
    else:
        newUser = userForm.save()
        login(newUser)
        request.session.update({'user':newUser.to_dict()})
        return JsonResponse(newUser.to_dict(),status=201)

def logIn(request):
    # data = request.body
    # dataObj = json.loads(data)
    username = request.POST['username']
    password = request.POST['password']
    # print(request.session['user'])
    user = authenticate(username = username,password = password)
    if user is not None:
        login(request,user)
        request.session.update({'user':user.to_dict()})
        response = JsonResponse({"user":user.to_dict()})
        return response
    else:
        return JsonResponse({"error":"incorrect credentials"})

def signOut(request):
    try:
        logout(request)
        return JsonResponse({"message":"logout successfully"})
    except Exception as e:
        return JsonResponse({"error":e})


class OwnerAppointmentsView(View):
    def get(self,request):
        data = json.loads(request.body)
        if('ownerId' not in data):
            return JsonResponse({'error':'bad request'})
        try:
            ownerId = data['ownerId']
            owner = Owner.objects.get(pk=ownerId)
            appointments = Appointment.objects.filter(owner = owner)
            response = JsonResponse({"appointments":[appointment.to_dict() for appointment in appointments]})
            return response
        except Owner.DoesNotExist:
            return JsonResponse({'error':'owner could not be found'})

    def post(self,request):
        companionId,appointment_address,walkerId,ownerId,start_time,end_time,status,appointment_notes,type,media_url = request.POST
        print(companionId)

class WalkerAppointmentsView(View):
    def get(self,request,*args,**kwargs):
        data = json.loads(request.body)
        if ('walkerId' not in data):
            return JsonResponse({'error':'Bad Request'},status = 400)
        try:
            walkerId = data['walkerId']
            walker = Walker.objects.get(pk = walkerId)
            appointments = Appointment.objects.filter(walker = walker)
            return JsonResponse({'appointments':[appointment.to_dict() for appointment in appointments]})
        except Walker.DoesNotExist:
            return JsonResponse({'error':'walker not found'})

class OneAppointmentView(View):
    def get(self,request,*args,**kwargs):
        appointmentId = kwargs['id']
        try:
            appointment = Appointment.objects.get(pk=appointmentId)
            return JsonResponse(appointment.to_dict())
        except Appointment.DoesNotExist:
            return JsonResponse({'message':'appointment not found'},status=404)


    def post(self,request):
        companionId,appointment_address,walkerId,ownerId,start_time,end_time,status,appointment_notes,type,media_url = request.POST
        print(companionId)
class CompanionsView(View):
    def get(self,request,*args,**kwargs):
        return

class OneCompanionView(View):
    def get(self,request,*args,**kwargs):
        return


# class
