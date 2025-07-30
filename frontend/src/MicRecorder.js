// MicRecorder.js
import React, { useState, useRef, useEffect } from 'react';

function MicRecorder({ onSend, resetSignal }) {
  const [recording, setRecording] = useState(false);
  const mediaRecorderRef = useRef(null);
  const audioChunksRef = useRef([]);

  const startRecording = async () => {
    try {
      const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
      const mediaRecorder = new MediaRecorder(stream);

      audioChunksRef.current = [];
      mediaRecorderRef.current = mediaRecorder;

      mediaRecorder.ondataavailable = (e) => {
        if (e.data.size > 0) {
          audioChunksRef.current.push(e.data);
        }
      };

      mediaRecorder.onstop = async () => {
        const audioBlob = new Blob(audioChunksRef.current, { type: 'audio/webm' });
        if (onSend) onSend(audioBlob);
      };

      mediaRecorder.start();
      setRecording(true);
    } catch (err) {
      alert('🎙️ Microphone access denied or not supported.');
    }
  };

  const stopRecording = () => {
    if (mediaRecorderRef.current) {
      mediaRecorderRef.current.stop();
      setRecording(false);
    }
  };

  useEffect(() => {
    setRecording(false);
    mediaRecorderRef.current = null;
    audioChunksRef.current = [];
  }, [resetSignal]);

  return (
    <>
      <button onClick={startRecording} disabled={recording}>🎙️ Start</button>
      <button onClick={stopRecording} disabled={!recording}>🛑 Stop</button>
    </>
  );
}

export default MicRecorder;
