using Microsoft.EntityFrameworkCore;

namespace backend.Models.Appointment;
class AppointmentContext : DbContext{
    public AppointmentContext (DbContextOptions<AppointmentContext> options) : base (options)
    {

    }
    public DbSet<Appointment> Appointments {get; set;} = null;
}
