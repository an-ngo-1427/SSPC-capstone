import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Header from "./components/Header";
import LandingPage from "./pages/LandingPage";
import Reservation from "./pages/Reservation";
import CompanionPage from "./pages/CompanionPage";

function App() {
  return (
    <Router>
      <Header />
      <Routes>
        <Route path="/" element={<LandingPage />} />
        <Route path="/reservation" element={<Reservation />} />
        <Route path="/companion" element={<CompanionPage />} />
      </Routes>
    </Router>
  );
}

export default App;
