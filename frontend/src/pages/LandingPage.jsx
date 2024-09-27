import React from "react";
import Hero from "../Components/Landing/Hero.jsx";
import Footer from "../Components/Landing/Footer";
import "/Users/giang/Pepper/frontend/src/App.css";
import pepperTrail from "/Users/giang/Pepper/frontend/src/assets/pepper-trail.jpeg";

const LandingPage = () => {
  return (
    <div>
      <Hero />

      <section
        className="info-section"
        style={{ backgroundImage: "url(/src/assets/pepper-trail.jpeg)" }}>
        <h2>Why Choose Pepper's Happy Trails?</h2>
        <p>
          We provide exceptional, loving care for your pets, giving them the attention they deserve.
        </p>
      </section>
      {/* <Footer /> */}
    </div>
  );
};

export default LandingPage;
