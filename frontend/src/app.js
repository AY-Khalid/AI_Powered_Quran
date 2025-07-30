// App.js
import React, { useState } from 'react';
import MicRecorder from './MicRecorder';
import './App.css';

function App() {
  const [transcript, setTranscript] = useState(null);
  const [result, setResult] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const [resetCounter, setResetCounter] = useState(0);

  const sendAudio = async (audioBlob) => {
    setIsLoading(true);
    setTranscript(null);
    setResult(null);

    const formData = new FormData();
    formData.append('file', audioBlob, 'recording.webm');

    try {
      const response = await fetch('http://localhost:8000/transcribe', {
        method: 'POST',
        body: formData,
      });

      const data = await response.json();
      setTranscript(data.transcript);
      setResult(data.match);
    } catch (error) {
      setTranscript("❌ Error during transcription.");
      setResult({ match_text: "Could not process the audio." });
    } finally {
      setIsLoading(false);
    }
  };

  const handleRefresh = () => {
    setTranscript(null);
    setResult(null);
    setIsLoading(false);
    setResetCounter(prev => prev + 1);
  };

  return (
    <div className="app-container">
      <h1>🎧 Quran Verse Recognition</h1>

      <div className="button-row">
        <MicRecorder onSend={sendAudio} resetSignal={resetCounter} />
        <button onClick={handleRefresh} className="refresh-button">🔄 Refresh</button>
      </div>

      <div className="transcript">
        <strong>📜 Transcription:</strong>
        <p>
          {isLoading
            ? 'Transcribing...'
            : transcript
            ? transcript
            : 'Nothing transcribed yet.'}
        </p>
      </div>

      <div className="result">
        <strong>🔍 Match:</strong>
        {isLoading ? (
          <p>Matching verse...</p>
        ) : result ? (
          result.text ? (
            <div className="match-container">
              <p>{result.match_text}</p>
              <p>🕋 Arabic: </p>
              <p className="arabic-text">{result.text}</p>
            </div>
          ) : (
            <p>{result.match_text}</p>
          )
        ) : (
          <p>No match yet.</p>
        )}
      </div>
    </div>
  );
}

export default App;
