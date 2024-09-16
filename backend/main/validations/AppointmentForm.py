from django import forms
from ..models import Appointment
class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields=['companion','appointment_address','walker','owner','start_time','end_time','status','appointment_notes','type','media_url']
        exclude=[]
    def clean(self):
        cleaned_data = super().clean()
        instance = self.instance
        data = instance.start_date
        print('printing from clear',data)
        # bookedAppt = Appointment.objects.filter(start_date = )
