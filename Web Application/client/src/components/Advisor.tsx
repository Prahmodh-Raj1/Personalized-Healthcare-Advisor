import React, { useState } from "react";
import "./Advisor.css";
import { FaArrowUp } from "react-icons/fa";

const Advisor: React.FC = () => {
  const [inputd, setInput] = useState("");
  
  // eslint-disable-next-line @typescript-eslint/no-unused-vars
  const [symptom_analysis, setSymptomAnalysis] = useState("");
  // Removed unused state variable medical_guidance
  const [medical_guidance, setMedicalGuidance] = useState("");
  const [lifestyle_recommendations, setLifestyleRecommendations] = useState("");

  const handleSubmit = async () => {
    if (!inputd.trim()) return;
    
    
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
      // Optionally show error to user
    } 
  };

  const handleGuidance = async()=>{
    if(!symptom_analysis.trim()){
      return;
    }
    try{
      console.log("Issuing request for medical guidance")
      const response = await fetch('http://localhost:8000/med_guidance',{
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

    }catch(error){
      console.error('Error:', error); 
    }
  };

  const handleLifestyle = async () => {
    if (!medical_guidance.trim()) {
      return;
    }
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
    }
  };

  return (
    <div className="health-advisor-container">
      <h1 className="logo">Health_Advisor</h1>
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
        {symptom_analysis && (
          <div className="result-section">
            <h3>Analysis</h3>
            <p>{symptom_analysis}</p>
            <button className="guidance-btn" onClick={handleGuidance}>
              Get Medical Guidance?
            </button>
          </div>
        )}
        {medical_guidance && (
          <div className="result-section">
            <h3>Medical Guidance</h3>
            <p>{medical_guidance}</p>
            <button className="guidance-btn" onClick={handleLifestyle}>
              Get Lifestyle Recs?
            </button>
          </div>
        )}
        {lifestyle_recommendations && (
          <div className="result-section">
            <h3>Lifestyle Recommendations</h3>
            <p>{lifestyle_recommendations}</p>
          </div>
        )}
      </div>
    </div>
  );
};

export default Advisor;

/*

{(results.analysis || results.guidance || results.lifestyle) && (
        <div className="results-container">
          {results.analysis && (
            <div className="result-section">
              <h3>Analysis</h3>
              <p>{results.analysis}</p>
            </div>
          )}
          {results.guidance && (
            <div className="result-section">
              <h3>Medical Guidance</h3>
              <p>{results.guidance}</p>
            </div>
          )}
          {results.lifestyle && (
            <div className="result-section">
              <h3>Lifestyle Recommendations</h3>
              <p>{results.lifestyle}</p>
            </div>
          )}
        </div>
      )}

      */
