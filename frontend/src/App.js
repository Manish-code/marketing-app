import React from 'react';
import LandingPage from './components/LandingPage';
import BlogPage from './components/BlogPage';
import ContactForm from './components/ContactForm';
import SignUpForm from './components/SignUpForm';

function App() {
  return (
    <div className="App">
      <LandingPage />
      <BlogPage />
      <ContactForm />
      <SignUpForm />
    </div>
  );
}

export default App;
