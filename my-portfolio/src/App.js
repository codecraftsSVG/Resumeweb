import React, { useState, useEffect } from 'react';

const App = () => {
  const [language, setLanguage] = useState('en'); // Default language is English
  const [showPopup, setShowPopup] = useState(false);

  useEffect(() => {
    // Detect browser language
    const browserLanguage = navigator.language.split('-')[0];
    setLanguage(browserLanguage);
  }, []);

  useEffect(() => {
    // Show popup after 5 seconds
    const timer = setTimeout(() => {
      setShowPopup(true);
    }, 5000);

    return () => clearTimeout(timer);
  }, []);

  return (
    <div>
      <header>
        <h1>Welcome to My Portfolio</h1>
      </header>
      
      <section>
        <h2>About Me</h2>
        {/* Add your skills and experience here */}
      </section>

      <section>
        <h2>Portfolio</h2>
        {/* Add your projects and demos here */}
      </section>

      <section>
        <h2>Contact</h2>
        {/* Add a contact form or details here */}
      </section>

      {/* Language popup */}
      {showPopup && (
        <div className="popup">
          <p>Thank you for visiting! You spent 5 seconds on this site.</p>
        </div>
      )}
    </div>
  );
};

export default App;
