using Microsoft.AspNetCore.Mvc;
using backend.Models.Appointment;
namespace backend.Controllers;

[ApiController]
[Route("api/[controller]")]

class AppointmentsController : ControllerBase
{
    private readonly AppointmentContext _context;
    public AppointmentsController(AppointmentContext context)
    {
        _context = context;
    }

    [HttpGet]
    public List<Appointment>GetAppointments(){

    }

    [HttpGet("{id}")]
    public Appointment GetAppointment([FromRoute] int id){
        Appointment appointment = _context.Appointments.SingleOrDefault(appointment=>appointment.Id == id);
        if(appointment == null){
            return
        }
    }
}
