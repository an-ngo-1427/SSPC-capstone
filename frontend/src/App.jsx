import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Header from "./Components/Landing/Header.jsx";
import Hero from "./Components/Landing/Hero.jsx";
import Footer from "./Components/Landing/Footer.jsx";
import LandingPage from "./pages/LandingPage.jsx";
import CompanionPage from "./pages/CompanionPage.jsx";
import Reservation from "./pages/Reservation.jsx";

function App() {
  return (
    <Router>
      <Header />

      {/* <Hero />
      <Footer /> */}

      <Routes>
        <Route path="/" element={<LandingPage />} />
        <Route path="/reservation" element={<Reservation />} />
        <Route path="/companion" element={<CompanionPage />} />
      </Routes>
    </Router>
  );
}

export default App;
