import { useState } from 'react'
import './App.css'

function App() {
  const [data, setData] = useState(null);

  const fetchData = () => {
    fetch('/api/data')
      .then(response => response.json())
      .then(fetchedData => setData(fetchedData))
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
          {data}
        </button>
        <p>
          Edit <code>src/App.tsx</code> and save to test HMR
        </p>
      </div>
      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p>
    </>
  )
}

export default App
