from django.urls import path
from .views import OwnerAppointmentsView,OneAppointmentView,signUp,signOut,logIn,getCsurf,CompanionsView,OneCompanionView,WalkerAppointmentsView,WalkersView
urlpatterns = [
    path('getcsrf/',getCsurf,name='get_csrf'),
    path('signup/',signUp,name='signup'),
    path('login/',logIn,name='login'),
    path('signout/',signOut,name='signout'),
    path('companions/',CompanionsView.as_view(),name='companions'),
    path('companions/<int:id>/',OneCompanionView.as_view()),
    path('owner/appointments/',OwnerAppointmentsView.as_view(),name='appointments'),
    path('walker/appointments/',WalkerAppointmentsView.as_view(),name='appointments'),
    path('appointments/<int:id/',OneAppointmentView.as_view(),name='one_appointment'),
    path('walkers/',WalkersView.as_view(),name='walkers')
]
