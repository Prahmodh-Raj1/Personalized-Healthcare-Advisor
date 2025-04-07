//@ts-nocheck
import React, { useState } from "react";
import "./Advisor.css";
import { FaArrowUp } from "react-icons/fa";
 // Add this import at the top

const Advisor: React.FC = () => {
  const [inputd, setInput] = useState("");

  
  const [symptom_analysis, setSymptomAnalysis] = useState("");
  const [medical_guidance, setMedicalGuidance] = useState("");
  const [lifestyle_recommendations, setLifestyleRecommendations] = useState("");

  const [isLoadingAnalysis, setIsLoadingAnalysis] = useState(false);
  const [isLoadingGuidance, setIsLoadingGuidance] = useState(false);
  const [isLoadingLifestyle, setIsLoadingLifestyle] = useState(false);

  const handleSubmit = async () => {
    if (!inputd.trim()) return;
    setIsLoadingAnalysis(true);
    try {
      console.log("Making post request")
      const response = await fetch('http://localhost:8000/symptoms', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ symptoms: inputd })
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data = await response.json();
      console.log("Retrieved response: ", data);
      setSymptomAnalysis(data);
    } catch (error) {
      console.error('Error:', error);
    } finally {
      setIsLoadingAnalysis(false);
    }
  };

  const handleGuidance = async () => {
    if (!symptom_analysis.trim()) {
      return;
    }
    setIsLoadingGuidance(true);
    try {
      console.log("Issuing request for medical guidance")
      const response = await fetch('http://localhost:8000/med_guidance', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ analysis: symptom_analysis })
      });
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      const data = await response.json();
      setMedicalGuidance(data);
    } catch (error) {
      console.error('Error:', error);
    } finally {
      setIsLoadingGuidance(false);
    }
  };

  const handleLifestyle = async () => {
    if (!medical_guidance.trim()) {
      return;
    }
    setIsLoadingLifestyle(true);
    try {
      console.log("Requesting lifestyle recommendations");
      const response = await fetch('http://localhost:8000/lifestyle', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ 
          analysis: symptom_analysis,
          guidance: medical_guidance 
        })
      });
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      const data = await response.json();
      setLifestyleRecommendations(data);
    } catch (error) {
      console.error('Error:', error);
    } finally {
      setIsLoadingLifestyle(false);
    }
  };

  return (
    <div className="health-advisor-container">
      <h1 className="logo">AI-Powered Wellness Insight System</h1>
      
      
      
    <div className="search-box">
      <input 
          type="text" 
          value={inputd}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Describe your symptoms or health concerns..." 
          className="search-input"
        />
        <button className="send-btn" onClick={handleSubmit}>
          <FaArrowUp className="icon" />
        </button>
      </div>
      <div className="results-container">
        {(symptom_analysis || isLoadingAnalysis) && (
          <div className="result-section">
            <h3>Symptom Analysis</h3>
            {isLoadingAnalysis ? (
              <div className="loader-container">
                <div className="loader"></div>
              </div>            ) : (
              <>
                
                  <p>{symptom_analysis}</p>
 
                {symptom_analysis && !isLoadingAnalysis && (
                  <button className="next-step-btn" onClick={handleGuidance}>
                    Get Medical Guidance? <span className="return-symbol">↵</span>
                  </button>
                )}
              </>
            )}
          </div>
        )}
        
        
        {(medical_guidance || isLoadingGuidance) && (
          <div className="result-section">
            <h3>Personalised Medical Guidance</h3>
            {isLoadingGuidance ? (
              <div className="loader-container">
                <div className="loader"></div>
              </div>
            ) :  (
              <>
              <p>{medical_guidance}</p>
              {medical_guidance && !isLoadingGuidance && (
                <button className="next-step-btn" onClick={handleLifestyle}>
            Get Lifestyle Recs? <span className="return-symbol">↵</span>
          </button>
              )}
              </>
            )}
            
          </div>
        )}
        
        
        {(lifestyle_recommendations || isLoadingLifestyle) && (
          <div className="result-section">
            <h3>Lifestyle Recommendations</h3>
            {isLoadingLifestyle ? (
              <div className="loader-container">
                <div className="loader"></div>
              </div>
            ) : (
              <p>{lifestyle_recommendations}</p>
            )}
          </div>
        )}
      </div>
    </div>
  );
};

export default Advisor;
