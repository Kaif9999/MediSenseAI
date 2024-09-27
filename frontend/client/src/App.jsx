import './App.css';
import Spline from '@splinetool/react-spline';

function App() {
  return (
    <div>
      {/* Navigation bar */}
      <div className="navbar">
        <h2>Health AI</h2>
        <ul>
          <li><a href="#home">Home</a></li>
          <li><a href="#about">About</a></li>
          <li><a href="#contact">Contact</a></li>
        </ul>
      </div>

      <div className="app-container">
        {/* Raining pills */}
        {[...Array(10)].map((_, index) => (
          <div className="pill" key={index}></div>
        ))}

        <div className="grid-container">
          <div className="text-description">
            <h1>Health AI</h1>
            <p>
              Welcome to our innovative health platform powered by AI. Explore
              the 3D model to learn more about human anatomy and health insights.
            </p>
            <div className="button-group">
              <button>Sign Up</button>
              <button>Login</button>
            </div>
          </div>
          <div className="spline-wrapper">
            <div className="spline-container">
              <Spline scene="https://prod.spline.design/WM4RIaeFZsDYRn4L/scene.splinecode" />
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
