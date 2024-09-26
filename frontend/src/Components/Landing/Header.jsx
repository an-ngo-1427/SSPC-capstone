import React from "react";
import { Link } from "react-router-dom";
import logo from "/assets/logo.png"; // Update to correct path

const Header = () => {
  return (
    <header className="header">
      <img src={logo} alt="Pepper's Happy Trails Logo" className="logo" />
      <nav>
        <ul className="nav-links">
          <li>
            <Link to="/">Home</Link>
          </li>
          <li>
            <Link to="/companion">Companion Info</Link>
          </li>
          <li>
            <Link to="/reservation">Reserve a Walk</Link>
          </li>
          <li>
            <Link to="/login">Login</Link>
          </li>
        </ul>
      </nav>
    </header>
  );
};

export default Header;
