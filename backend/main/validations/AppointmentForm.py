from django import forms
from ..models import Appointment
from datetime import datetime
class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields=['companion','appointment_address','walker','owner','start_time','end_time','status','appointment_notes','type','media_url']
        exclude=[]
    def clean(self):
        cleaned_data = super().clean()
        start_time = cleaned_data.get('start_time')
        end_time = cleaned_data.get('end_time')
        dateFormat = '%Y-%m-%d %H:%M'

        bookedAppts = Appointment.objects.filter(start_time = start_time).order_by(start_time)

        # bookedAppt = Appointment.objects.filter(start_date = )

        def isValidSlot(targetSlot,scheduledSlots):
            isValid = True
            for slot in scheduledSlots:
                startTime = slot.start_time
                endTime = slot.end_time
                if(targetSlot.start_time < endTime and targetSlot.end_time > startTime ):
                    isValid = False

            return isValid
