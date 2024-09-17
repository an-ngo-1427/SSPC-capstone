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
from .validations.WalkerForm import WalkerForm
from .validations.AppointmentForm import AppointmentForm
from .validations.CompanionForm import CompanionForm
import json
from django.shortcuts import get_object_or_404
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
            errObj[field] = error[0].message
        return JsonResponse({'error':errObj},status=400)
    else:
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']

        newUser = User.objects.create_user(username,email,password,first_name=first_name,last_name = last_name)
        Owner.objects.create(user=newUser)
        login(request,newUser)
        return JsonResponse(newUser.to_dict())

def logIn(request):
    # data = request.body
    # dataObj = json.loads(data)
    username = request.POST['username']
    password = request.POST['password']
    print(request.user)
    print(username,password)
    user = authenticate(request,username = username,password = password)
    print(user)
    if user is not None:
        login(request,user)
        request.session.update({'user':user.to_dict()})
        response = JsonResponse({"user":user.to_dict()})
        return response
    else:
        return JsonResponse({"error":"incorrect credentials"},status=400)

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
            owner = Owner.objects.get(user__username = request.user)
            print(owner)
            appointments = Appointment.objects.filter(owner = owner)
            response = JsonResponse({"appointments":[appointment.to_dict() for appointment in appointments]})
            return response
        except Owner.DoesNotExist:
            return JsonResponse({'error':'owner could not be found'})

    def post(self,request):
        companionId= request.POST['companionId']
        walkerId  = request.POST['walkerId']

        appointmentObj = request.POST.dict()

        companion = Companion.objects.get(pk = companionId)
        owner = Owner.objects.get(user__username=request.user)
        walker = Walker.objects.get(pk = walkerId)

        appointmentObj['companion'] = companion
        appointmentObj['owner'] = owner
        appointmentObj['walker'] = walker
        appointmentForm = AppointmentForm(appointmentObj)

        if(not appointmentForm.is_valid()):
            errObj = {}
            errors = appointmentForm.errors.as_data()
            print(errors)
            for field,error in errors.items():
                errObj[field] = error[0].message

            return JsonResponse(errObj,status=400)
        else:
            newAppt = appointmentForm.save()
            return JsonResponse(newAppt.to_dict(),status=201)



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
class WalkersView(View):
    def get(self,request):
        walkers = Walker.objects.all().order_by('start_time')
        return JsonResponse({'walkers':[walker.to_dict() for walker in walkers]})

    def post(self,request):

        try:
            user = User.objects.get(username=request.user)
            # walker = Walker.objects.create(user=user,bio=request.POST['bio'],certified = False)
            dataObj = {'user':user,'bio':request.POST['bio'],'certified':False}
            walkerForm = WalkerForm(dataObj)

            if walkerForm.is_valid():
                walker = walkerForm.save()
                return JsonResponse({'walker':walker.to_dict()})
            else:
                errObj = {}
                errors = walkerForm.errors.as_data()
                for field,error in errors.items():
                    errObj[field] = error[0].message

                print('this is error',errObj)
                return JsonResponse({'error':errObj})
        except User.DoesNotExist:
            return JsonResponse({'error':'user not found'},status = 404)


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
    def get(self,request):
        user = get_object_or_404(User,username = request.user)
        companions = Companion.objects.filter(owner__user=user)
        return JsonResponse({'companions':[companion.to_dict() for companion in companions]})
    def post(self,request):
        try:
            user = User.objects.get(username = request.user)
            owner = Owner.objects.get(user = user)
            obj = request.POST.dict()
            obj['owner'] = owner

            print(obj)
            companionForm = CompanionForm(obj)

            if(companionForm.is_valid()):
                companion = companionForm.save()
                return JsonResponse(companion.to_dict())
            else:
                errObj = {}
                errors = companionForm.errors.as_data()
                for field,error in errors.items():
                    print(field,error)
                    errObj[field] = error[0].message
                return JsonResponse(errObj,status = 400)
        except Owner.DoesNotExist:
            return JsonResponse({'error':'owner could not be found'},status = 404)


class OneCompanionView(View):
    def get(self,request,*args,**kwargs):
        return


# class
