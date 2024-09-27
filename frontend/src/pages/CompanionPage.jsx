import React, { useState } from "react";

const CompanionPage = () => {
  const [companionInfo, setCompanionInfo] = useState({
    name: "",
    age: "",
    breed: "",
    specialNeeds: "",
  });

  const handleChange = (e) => {
    setCompanionInfo({
      ...companionInfo,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    alert(
      `Companion Info: ${companionInfo.name}, Age: ${companionInfo.age}, Breed: ${companionInfo.breed}, Special Needs: ${companionInfo.specialNeeds}`
    );
  };

  return (
    <form onSubmit={handleSubmit} className="companion-form">
      <h2>Enter Companion Information</h2>
      <input type="text" name="name" placeholder="Pet's Name" onChange={handleChange} required />
      <input type="number" name="age" placeholder="Age" onChange={handleChange} required />
      <input type="text" name="breed" placeholder="Breed" onChange={handleChange} required />
      <textarea name="specialNeeds" placeholder="Special Needs" onChange={handleChange}></textarea>
      <button type="submit">Save Info</button>
    </form>
  );
};

export default CompanionPage;
