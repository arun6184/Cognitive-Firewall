import React, { useState } from 'react';

const API_URL = "/api/analyze";

function App() {
  const [inputText, setInputText] = useState("");
  const [result, setResult] = useState(null);

  const handleSubmit = async () => {
    try {
      const response = await fetch(API_URL, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ text: inputText }),
      });

      const data = await response.json();
      console.log("API response:", data);
      setResult(data);
    } catch (error) {
      console.error("API error:", error);
    }
  };

  return (
    <div style={{ padding: '20px' }}>
      <h1>Cognitive Firewall</h1>
      
      <textarea
        value={inputText}
        onChange={(e) => setInputText(e.target.value)}
        placeholder="Enter text to analyze"
        rows={6}
        cols={50}
        style={{ marginBottom: '10px' }}
      />
      <br />
      
      <button onClick={handleSubmit}>Analyze</button>

      {result && (
        <div style={{ marginTop: '20px' }}>
          <h2>Result</h2>
          <p><strong>Text:</strong> {result.text}</p>
          <p><strong>Classification:</strong> {result.classification}</p>
          <p><strong>Confidence:</strong> {result.confidence}</p>
          <p><strong>Entities:</strong> {result.entities.length > 0 ? result.entities.join(", ") : "None"}</p>
          <p><strong>Flags:</strong> {result.flags.length > 0 ? result.flags.join(", ") : "None"}</p>
        </div>
      )}
    </div>
  );
}

export default App;
