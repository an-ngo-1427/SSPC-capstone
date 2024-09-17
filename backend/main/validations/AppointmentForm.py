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

        # filter parameters (looking at a specific date for a specific companion)
        specificDate = start_time.date()
        companion = cleaned_data.get('companion')
        bookedAppts = Appointment.objects.filter(start_time__date = specificDate,companion__id=companion.id).order_by('start_time')

        if(end_time < start_time):
            raise forms.ValidationError(("end time is before start time"))
        if( not self.isValidSlot(start_time,end_time,bookedAppts)):
            raise forms.ValidationError(("scheduled appointments conflict"))

    def isValidSlot(self,start_time,end_time,scheduledSlots):
        isValid = True
        for slot in scheduledSlots:
            startTime = slot.start_time
            endTime = slot.end_time
            if(start_time < endTime and end_time >= startTime ):
                isValid = False
                break
        return isValid
