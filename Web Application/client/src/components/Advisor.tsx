import React from "react";
import "./Advisor.css";
import { FaArrowUp } from "react-icons/fa";  // Remove FaPaperclip import

const Advisor: React.FC = () => {
  return (
    <div className="health-advisor-container">
      <h1 className="logo">Health_Advisor</h1>
      <div className="search-box">
        <input 
          type="text" 
          placeholder="Describe your symptoms or health concerns..." 
          className="search-input"
        />
        <button className="send-btn">
          <FaArrowUp className="icon" />
        </button>
      </div>
      
    </div>
  );
};

export default Advisor;
