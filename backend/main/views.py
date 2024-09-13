from django.shortcuts import render
from django.views import View
from django.http import JsonResponse,HttpResponse
from .models import Appointment,Companion,User,Owner
from django.views.decorators.csrf import ensure_csrf_cookie
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate, login,logout
import json
from django.core.serializers import serialize
# Create your views here.
@ensure_csrf_cookie
def getCsurf(request):
    cookies = request.COOKIES.get('csrftoken')
    response = JsonResponse({'csrfToken':cookies})
    return response

def signUp(request):
    data = request.body
    dataObj = json.loads(data)
    username = dataObj['username']
    email = dataObj['email']
    password = dataObj['password']
    first_name = dataObj['firstname']
    last_name = dataObj['lastname']

    try:
        newUser = User.objects.create_user(username = username,email = email,password = password,first_name = first_name,last_name = last_name)

        login(request,newUser)
        request.session.update({'user':newUser.to_dict()})
        response = JsonResponse({"user":newUser.to_dict()})
        return response
    except ValueError:
        JsonResponse({'error':"there was an error"})

def logIn(request):
    data = request.body
    dataObj = json.loads(data)
    username = dataObj['username']
    password = dataObj['password']
    print(request.session['user'])
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
    def get(self,request,*args,**kwargs):
        data = json.loads(request.body)
        if('ownerId' not in data):
            return JsonResponse({'error':'bad request'})
        try:
            ownerId = data['ownerId']
            owner = Owner.objects.get(pk=ownerId)
            if(not owner):
                return JsonResponse({'error':'owner could not be found'})

            appointments = Appointment.objects.filter(owner = owner)

            response = JsonResponse({"appointments":[appointment.to_dict() for appointment in appointments]})
            return response
        except Owner.DoesNotExist:
            return JsonResponse({'error':'owner could not be found'})


    def post(self,request,*args,**kwargs):
        print('post',args,kwargs)

class WalkerAppointmentsView(View):
    def get():
        return
class OneAppointmentView(View):
    def get(self,request,*args,**kwargs):
        print('get one',args,kwargs)
        return

    def post(self,request,*args,**kwargs):
        print('post one',args,kwargs)
        return

class CompanionsView(View):
    def get(self,request,*args,**kwargs):
        return

class OneCompanionView(View):
    def get(self,request,*args,**kwargs):
        return


# class
