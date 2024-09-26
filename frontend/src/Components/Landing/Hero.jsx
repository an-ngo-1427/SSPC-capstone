import React from "react";
import heroImage from "./assets/dog-walking.jpg"; // Hero background image

const Hero = () => {
  return (
    <section className="hero" style={{ backgroundImage: `url(${heroImage})` }}>
      <div className="hero-content">
        <h1>Welcome to Pepper's Happy Trails</h1>
        <p>lonely pets no more, a caring friend for your best friend</p>
        <button className="cta-button">
          <a href="/reservation">Join our Trail</a>
        </button>
      </div>
    </section>
  );
};

export default Hero;
