import React, { useState } from 'react';

function App() {
  const [file, setFile] = useState<File | null>(null);
  const [range, setRange] = useState({ start: 0, end: 10 });
  const [loading, setLoading] = useState(false);

  const handleUpload = async () => {
    if (!file) return;
    setLoading(true);

    const formData = new FormData();
    formData.append('file', file);
    formData.append('start', range.start.toString());
    formData.append('end', range.end.toString());

    try {
      const res = await fetch('http://localhost:8000/process', {
        method: 'POST',
        body: formData,
      });
      const data = await res.json();
      alert(`Exported to: ${data.file}`);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ padding: '40px', fontFamily: 'sans-serif' }}>
      <h1>Custom Video Editor</h1>
      
      <input type="file" onChange={(e) => setFile(e.target.files?.[0] || null)} />
      
      <div style={{ margin: '20px 0' }}>
        <label>Start (sec): </label>
        <input type="number" value={range.start} 
               onChange={e => setRange({...range, start: +e.target.value})} />
        
        <label style={{ marginLeft: '10px' }}>End (sec): </label>
        <input type="number" value={range.end} 
               onChange={e => setRange({...range, end: +e.target.value})} />
      </div>

      <button onClick={handleUpload} disabled={loading}>
        {loading ? 'Processing...' : 'Trim & Export'}
      </button>
    </div>
  );
}

export default App;