import React, { useState, useEffect } from 'react'

function App() {
  const [data, setData] = useState([{}])

  useEffect(() => {
    fetch("/lens_data").then(
      res => res.json()
    ).then(
      data => {
        setData(data)
        console.log(data)
      }
    )

  }, [])
  return (
    <div>
      {(typeof data.lenses === 'undefined') ? (
        <p>Loading...</p>) : (
        data.lenses.map((lens, i) => (
          <p key={i}>{lens}</p>
        )))}
    </div>
  )
}

export default App