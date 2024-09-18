from django import forms
from ..models import Appointment
from datetime import datetime
class CreateAppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields=['companion','appointment_address','walker','owner','start_time','end_time','status','appointment_notes','type','media_url']
        exclude=[]
    def clean(self):
        cleaned_data = super().clean()
        start_time = cleaned_data.get('start_time')
        end_time = cleaned_data.get('end_time')
        walker = cleaned_data.get('walker')
        specificDate = start_time.date()

        if(start_time is None):
            raise forms.ValidationError('start date required')
        if(end_time is None):
            raise forms.ValidationError('end date is required')
        if(end_time <= start_time):
            raise forms.ValidationError(("end time is before start time"))
        walkerBookedAppts = Appointment.objects.filter(start_time__date = specificDate,walker = walker).order_by('start_time')
        if( not self.isValidSlot(start_time,end_time,walkerBookedAppts)):
            raise forms.ValidationError("scheduled appointments conflicts")

    def isValidSlot(self,start_time,end_time,scheduledSlots):
        isValid = True
        for slot in scheduledSlots:
            startTime = slot.start_time
            endTime = slot.end_time
            if(start_time < endTime and end_time >= startTime ):
                isValid = False
                break
        return isValid
