import React, { useState } from "react";
import heroImage from "/Users/giang/Pepper/frontend/src/assets/dog-walking.jpg";

const Reservation = () => {
  const [reservation, setReservation] = useState({
    name: "",
    petName: "",
    date: "",
    time: "",
    location: "",
  });

  const handleChange = (e) => {
    setReservation({
      ...reservation,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    alert(
      `Reservation submitted: ${reservation.name}, Pet: ${reservation.petName}, Date: ${reservation.date}, Time: ${reservation.time}, Location: ${reservation.location}`
    );
  };

  return (
    <div className="reservation-container" style={{ backgroundImage: `url(${heroImage})` }}>
      <h2 className="reservation-header">Reserve a Walk</h2>
      <form onSubmit={handleSubmit} className="reservation-form">
        <div className="who">
          <input
            id="who-owner"
            type="text"
            name="name"
            placeholder="Your Name"
            onChange={handleChange}
            required
          />
          <input
            id="who-pet"
            type="text"
            name="petName"
            placeholder="Pet's Name"
            onChange={handleChange}
            required
          />
        </div>
        <div className="when">
          <input id="when-date" type="date" name="date" onChange={handleChange} required />
          <input id="when-time" type="time" name="time" onChange={handleChange} required />
        </div>
        <div className="where">
          <input
            type="text"
            name="location"
            placeholder="Location"
            onChange={handleChange}
            required
          />
        </div>
        <button type="submit">Submit</button>
      </form>
    </div>
  );
};

export default Reservation;
