import React from "react";
import "/Users/giang/Pepper/frontend/src/App.css";

const Footer = () => {
  return (
    <footer className="footer">
      <div>
        <nav>
          <a href="">Private Policy</a>
          <a href="">Terms of Service</a>
          <a href="">Contact Us</a>
          <a className="social-media" href="http://instagram.com">
            Instagram
          </a>
          <a className="social-media" href="http://youtube.com">
            YouTube
          </a>
        </nav>
        <p>© 2024 Pepper's Happy Trails. All Rights Reserved.</p>
      </div>
    </footer>
  );
};

export default Footer;
