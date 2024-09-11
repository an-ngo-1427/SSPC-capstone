namespace backend.Models.Appointment;
class Appointment{
    public int Id {get; set; }
    public int Companion_id {get; set;}
    public required string Appointment_address {get; set;}
    public required int Walker_id {get; set;}
    public required DateTime Start_time {get; set;}
    public required DateTime End_time {get; set;}
    public required string Status {get; set;}
    public string? Appointment_note {get; set;}
    public required string Type{get; set;}
    public string? Media_url {get; set;}

    public required DateTime Created_at {get; set;}
    public required DateTime Updated_at {get; set;}
}
