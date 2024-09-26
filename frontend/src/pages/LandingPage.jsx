import React from "react";
import Hero from "../components/Hero";
import Footer from "../components/Footer";

const LandingPage = () => {
  return (
    <>
      <Hero />
      <section className="info-section">
        <h2>Why Choose Pepper's Happy Trails?</h2>
        <p>
          We provide exceptional, loving care for your pets, giving them the attention they deserve.
        </p>
      </section>
      <Footer />
    </>
  );
};

export default LandingPage;
