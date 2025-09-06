import { useState } from 'react'
import './App.css'

function App() {
  const [data, setData] = useState<string | null>(null);

  const fetchData = () => {
    fetch('http://localhost:8000/api/data')
      .then(response => response.json())
      .then(fetchedData => setData(JSON.stringify(fetchedData, null, 2)))
      .catch(error => console.error('error during get data', error));
  }

  const handleButtonClick = () => {
    fetchData();
  }

  return (
    <>
      <h1>LLM Game Project</h1>
      <div className="card">
        <button onClick={handleButtonClick}>
        </button>
        <p>
          {data}
        </p>
      </div>
      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p>
    </>
  )
}

export default App
