
from django.views import View
from django.http import JsonResponse
from .models import Appointment,Companion,User,Owner,Walker
from django.views.decorators.csrf import ensure_csrf_cookie
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate, login,logout
from .validations.UserForm import UserForm
from .validations.WalkerForm import WalkerForm
from .validations.CreateAppointmentForm import CreateAppointmentForm
from.validations.UpdateAppointmentForm import UpdateAppointmentForm
from .validations.CompanionForm import CompanionForm
import json
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.utils.functional import wraps
def auth_decorator(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        # code to be executed before the view
        if(not request.user.is_authenticated):
            return JsonResponse({'error':'Forbidden'},status=403)
        response = view_func(request, *args, **kwargs)
        # code to be executed after the view
        return response
    return wrapper
# Create your views here.
@ensure_csrf_cookie
def getCsurf(request):
    cookies = request.COOKIES.get('csrftoken')
    response = JsonResponse({'csrfToken':cookies})
    return response
@ensure_csrf_cookie
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
@ensure_csrf_cookie
def logIn(request):
    # data = request.body
    # dataObj = json.loads(data)
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request,username = username,password = password)

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
    @method_decorator(auth_decorator)
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




class WalkerAppointmentsView(View):
    @method_decorator(auth_decorator)
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

    @method_decorator(auth_decorator)
    def post(self,request,*args,**kwargs):
        walker = get_object_or_404(Walker,user__username = request.user)
        appointmentObj = request.POST.dict()
        appointmentObj['walker'] = walker
        createAppointmentForm = CreateAppointmentForm(appointmentObj)
        if(createAppointmentForm.is_valid()):
            createAppointmentForm.save()
            appointments = Appointment.objects.filter(walker = walker).order_by('start_time')
            return JsonResponse({'appointments':[appointment.to_dict() for appointment in appointments]},status=201)
        else:
            errObj = {}
            errors = createAppointmentForm.errors.as_data()
            for field,error in errors.items():
                errObj[field] = error[0].message
            return JsonResponse(errObj,status = 400)

class WalkersView(View):
    def get(self,request):
        walkers = Walker.objects.all()
        return JsonResponse({'walkers':[walker.to_dict() for walker in walkers]})

    @method_decorator(auth_decorator)
    def post(self,request):

        try:
            user = User.objects.get(username=request.user)
            # walker = Walker.objects.create(user=user,bio=request.POST['bio'],certified = False)
            walkerObj = request.POST.dict()
            walkerObj['user'] = user

            walkerForm = WalkerForm(walkerObj)

            if walkerForm.is_valid():
                walker = walkerForm.save()
                return JsonResponse({'walker':walker.to_dict()},status=201)
            else:
                errObj = {}
                errors = walkerForm.errors.as_data()
                for field,error in errors.items():
                    errObj[field] = error[0].message
                return JsonResponse({'error':errObj},status=400)
        except User.DoesNotExist:
            return JsonResponse({'error':'user not found'},status = 404)


class OneAppointmentView(View):
    @method_decorator(auth_decorator)
    def get(self,request,*args,**kwargs):
        appointmentId = kwargs['id']
        try:
            appointment = Appointment.objects.get(pk=appointmentId)
            appointment = get_object_or_404(Appointment,owner__user__username = request.user)
            return JsonResponse(appointment.to_dict())
        except Appointment.DoesNotExist:
            return JsonResponse({'message':'appointment not found'},status=404)

    @method_decorator(auth_decorator)
    def post(self,request,*arg,**kwargs):
        companionId = request.POST['companionId']
        appointmentId = kwargs['id']
        appointment = get_object_or_404(Appointment,id=appointmentId)
        companion = get_object_or_404(Companion,id=companionId)

        appointmentObj = request.POST.dict()
        appointmentObj['companion'] = companion
        appointmentObj['owner'] = companion.owner

        updateAppointmentForm = UpdateAppointmentForm(appointmentObj,instance = appointment)

        if(not updateAppointmentForm.is_valid()):
            errObj = {}
            errors = updateAppointmentForm.errors.as_data()
            print(errors)
            for field,error in errors.items():
                errObj[field] = error[0].message

            return JsonResponse(errObj,status=400)
        else:
            newAppt = updateAppointmentForm.save()
            return JsonResponse(newAppt.to_dict(),status=201)



class CompanionsView(View):

    @method_decorator(auth_decorator)
    def get(self,request):
        user = get_object_or_404(User,username = request.user)
        companions = Companion.objects.filter(owner__user=user)
        return JsonResponse({'companions':[companion.to_dict() for companion in companions]})

    @method_decorator(auth_decorator)
    def post(self,request):
        try:
            user = User.objects.get(username = request.user)
            owner = Owner.objects.get(user = user)
            obj = request.POST.dict()
            obj['owner'] = owner

            companionForm = CompanionForm(obj)

            if(companionForm.is_valid()):
                companionForm.save()
                companions = Companion.objects.filter(owner=owner)
                return JsonResponse({'companions':[companion.to_dict() for companion in companions]},status=201)
            else:
                errObj = {}
                errors = companionForm.errors.as_data()
                for field,error in errors.items():
                    errObj[field] = error[0].message
                return JsonResponse(errObj,status = 400)
        except Owner.DoesNotExist:
            return JsonResponse({'error':'owner could not be found'},status = 404)



class OneCompanionView(View):
    @method_decorator(auth_decorator)
    def get(self,request,*args,**kwargs):
        owner = get_object_or_404(Owner,user__username = request.user)
        companion = get_object_or_404(Companion,pk=kwargs['id'],owner = owner)
        return JsonResponse(companion.to_dict())
    @method_decorator(auth_decorator)
    def delete(self,request,**kwargs):
        owner = get_object_or_404(Owner,user__username = request.user)
        companion = get_object_or_404(Companion,pk=kwargs['id'],owner = owner)

        companion.delete()
        return JsonResponse({'message':'companion successfully deleted'})


# class
# def auth_decorator(view_func):
#     def wrapper(request, *args, **kwargs):
#         # code to be executed before the view
#         print(request.user)
#         response = view_func(request, *args, **kwargs)
#         # code to be executed after the view
#         return response
#     return wrapper
