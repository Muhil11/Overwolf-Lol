import React, { useState } from "react";
import axios from "axios";

export default function App() {
  const [matchStats, setMatchStats] = useState({
    kills: "",
    deaths: "",
    assists: "",
    cs: "",
  });

  const [analysis, setAnalysis] = useState(null);

  const handleChange = (e) => {
    setMatchStats({ ...matchStats, [e.target.name]: e.target.value });
  };

  const analyzeMatch = async () => {
    try {
      const response = await axios.post("http://127.0.0.1:5000/analyze-match", matchStats);
      setAnalysis(response.data);
    } catch (error) {
      console.error("Error analyzing match:", error);
    }
  };

  return (
    <div style={{ padding: "20px", fontFamily: "Arial, sans-serif" }}>
      <h1>Champion Coach AI</h1>
      <p>Enter your match stats to get AI-powered insights!</p>

      <input type="number" name="kills" placeholder="Kills" onChange={handleChange} />
      <input type="number" name="deaths" placeholder="Deaths" onChange={handleChange} />
      <input type="number" name="assists" placeholder="Assists" onChange={handleChange} />
      <input type="number" name="cs" placeholder="Creep Score (CS)" onChange={handleChange} />

      <button onClick={analyzeMatch}>Analyze Match</button>

      {analysis && (
        <div>
          <h3>AI Insights:</h3>
          <p>Win Probability: {analysis.win_probability}%</p>
          <ul>
            {analysis.suggestions.map((suggestion, index) => (
              <li key={index}>{suggestion}</li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}
