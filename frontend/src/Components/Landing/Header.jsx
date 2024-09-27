import React from "react";
import { Link } from "react-router-dom";
import logo from "/assets/stocklogo.jpeg";
import "/Users/giang/Pepper/frontend/src/App.css";

function Header() {
  return (
    <header className="header">
      <img src={logo} alt="Pepper's Happy Trails Logo" className="logo" />
      <nav>
        <ul className="nav-links">
          <li>
            <Link to="/">Home</Link>
          </li>
          <li>
            <Link to="/about">About Us</Link>
          </li>
          <li>
            <Link to="/reservation">Join our Trail</Link>
          </li>
        </ul>
      </nav>
      <div>
        <button>
          <Link to="/login">Login</Link>
        </button>
      </div>
    </header>
  );
}

export default Header;
