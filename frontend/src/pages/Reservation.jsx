import React, { useState } from "react";

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
    <form onSubmit={handleSubmit} className="reservation-form">
      <h2>Reserve a Walk</h2>
      <input type="text" name="name" placeholder="Your Name" onChange={handleChange} required />
      <input type="text" name="petName" placeholder="Pet's Name" onChange={handleChange} required />
      <input type="date" name="date" onChange={handleChange} required />
      <input type="time" name="time" onChange={handleChange} required />
      <input type="text" name="location" placeholder="Location" onChange={handleChange} required />
      <button type="submit">Submit Reservation</button>
    </form>
  );
};

export default Reservation;
