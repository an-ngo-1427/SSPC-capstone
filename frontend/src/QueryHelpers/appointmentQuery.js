import Cookies from 'js-cookie'
import { MyError } from './sessionQuery'

export async function getOwnerAppointments(){
    const response = await fetch('api/owner/appointments')
    const data = await response.json()
    return data
}

export async function bookAppointment({appointmentId,formData}){

    console.log('booking appointment',formData)
    const response = await fetch(`api/appointments/${appointmentId}/`,{
        method:'POST',
        headers:{
            'X-CSRFToken':Cookies.get('csrftoken')
        },
        body:formData
    })

    const data = await response.json()
    if(response.ok){
        return data
    }else{
        throw new MyError(data.error)
    }
}
