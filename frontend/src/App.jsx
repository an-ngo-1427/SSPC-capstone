import React from "react";
import "./App.css";

import { useState } from "react";

function App() {
  return (
    <div className="App">
      <header className="header">
        <nav className="nav">
          <h1 className="logo">Pepper's Happy Trails</h1>
          <ul className="nav-links">
            <li>
              <a href="#appointments">Reserve your walk!</a>
            </li>
            <li>
              <a href="#about">Who me?</a>
            </li>
            <li>
              <a href="#contact"></a>Contact
            </li>
          </ul>
        </nav>
      </header>

      <section className="hero">
        <h2>Walk with the Earth</h2>
        <p>Your dog's best friend in an eco-conscious world. </p>
        <button className="cta-button">Reserve your Walk!</button>
      </section>

      <footer className="footer">
        <p>&copy; 2024 Pepper's Happy Trails. All rights reserved.</p>
      </footer>
    </div>
  );
}

export default App;

/*
import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <div>
        <a href="https://vitejs.dev" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
        <a href="https://react.dev" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>
      <h1>Vite + React</h1>
      <div className="card">
        <button onClick={() => setCount((count) => count + 1)}>
          count is {count}
        </button>
        <p>
          Edit <code>src/App.jsx</code> and save to test HMR
        </p>
      </div>
      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p>
    </>
  )
}

export default App
*/
